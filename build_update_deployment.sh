#!/bin/env bash

imageTag="study/flask-calculator:0.0.6"

minikube image build -t "$imageTag" .

yq -yi --arg imageTag "$imageTag" '.spec.template.spec.containers[0].image = $imageTag' deployment.yaml

kubectl apply -f deployment.yaml