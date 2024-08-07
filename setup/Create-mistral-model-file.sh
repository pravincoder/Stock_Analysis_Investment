#!/bin/bash

# Variables
model_name='mistral:latest'
custom_model_name='crewai_mistral'

# Get the model file
ollama pull $model_name

# Create model file
ollama create $custom_model_name -f ./MistralModelfile