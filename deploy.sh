#!/bin/env bash

environment=$1

kubectl apply -k "kustomize/overlays/$environment"
