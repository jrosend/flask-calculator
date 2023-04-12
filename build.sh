#!/bin/env bash

deploymentFile=kustomize/base/deployment.yaml

imageTag=$(yq -er ".spec.template.spec.containers[0].image" < $deploymentFile)

echo "Current image tag: $imageTag"

IFS=':' read -ra tagComponents <<< "$imageTag"
tag=${tagComponents[1]}
IFS='.' read -ra versionComponents <<< "$tag"
majorMinor="${versionComponents[0]}.${versionComponents[1]}"
patch=$((versionComponents[2]+1))
newTag="$majorMinor.$patch"
newImageTag="${tagComponents[0]}:$newTag"

echo "New image tag: $newImageTag"

minikube image build -t "$newImageTag" .

yq -yi --arg newImageTag "$newImageTag" '.spec.template.spec.containers[0].image = $newImageTag' $deploymentFile
