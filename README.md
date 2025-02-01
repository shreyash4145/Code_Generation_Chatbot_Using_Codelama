# CodeLlama Code Generator

This project is an automatic code generator and coding assistant chatbot using Meta's CodeLlama. It provides a Streamlit-based web UI for generating code from natural language prompts.

## Features
- Code generation using CodeLlama
- Streamlit web UI
- Dockerized deployment

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/code-generator-llama.git
   cd code-generator-llama
2. Install the required dependencies: ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run deployment/app.py
   ```

## Usage
1. Open your web browser and navigate to `http://localhost:8501`
2. Enter a natural language prompt in the input field
3. Click the "Generate Code" button to generate code

## Docker Deployment Configuration 
To deploy the application using Docker, you need to create a Dockerfile in the root directory of your
project. Here's an example Dockerfile:
dockerfile
docker build -t code-generator-llama .
docker run -p 8501:8501 code-generator-llama# Code_Generation_Chatbot_Using_Codelama
