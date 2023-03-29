#!/bin/env bash

imageTag=$(yq -er ".spec.template.spec.containers[0].image" < deployment.yaml)

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

yq -yi --arg newImageTag "$newImageTag" '.spec.template.spec.containers[0].image = $newImageTag' deployment.yaml

kubectl apply -f deployment.yaml
kubectl apply -f loadBalancerService.yaml
kubectl apply -f hpa.yaml
