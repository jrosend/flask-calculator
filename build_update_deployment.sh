#!/bin/env bash

imageTag="study/flask-calculator:0.0.7"

imageTag=$(yq -er ".spec.template.spec.containers[0].image" < deployment.yaml)

IFS=':' read -ra tagComponents <<< "$imageTag"
tag=${tagComponents[1]}
IFS='.' read -ra versionComponents <<< "$tag"
majorMinor="${versionComponents[0]}.${versionComponents[1]}"
patch=$((versionComponents[2]+1))
newTag="$majorMinor.$patch"
newImageTag="${tagComponents[0]}:$newTag"

minikube image build -t "$newImageTag" .

kubectl apply -f deployment.yaml

yq -yi --arg newImageTag "$newImageTag" '.spec.template.spec.containers[0].image = $newImageTag' deployment.yaml