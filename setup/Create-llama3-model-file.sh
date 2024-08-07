#!/bin/bash

# Variables
model_name='llama3'
custom_model_name='crewai_llama3_model1'

# Get the model file
ollama pull $model_name

# Create model file
ollama create $custom_model_name -f ./Llama3Modelfile