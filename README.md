# Employee Assistant

This project is a Neo4j-backed Chatbot using Python, designed to assist with employee-related queries and tasks.

## Prerequisites

Before running the application, ensure you have the following:

1. Python installed on your system
2. Neo4j database set up and running
3. Ollama installed on your computer (from [ollama.com](https://ollama.com))
4. Access to Google Colab (for hosting Ollama)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Apex-CS/Employee-Assistant.git
   ```

2. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

## Setup

1. Download the `Hosting_ollama-2.ipynb` file (provided separately).

2. Open Google Colab and select a T4 GPU Python3 environment.

3. Upload the `Hosting_ollama-2.ipynb` file to Colab and run all cells.

4. Copy the URL ending with `ngrok-free-app` from the Colab output.

5. Open the `llm.py` file in the project repository and paste the copied URL into the `ollama_emb` and `llm` variables.

6. Open a terminal and set the `OLLAMA_HOST` environment variable:
   ```
   export OLLAMA_HOST="YOUR_NGROK_URL_HERE"
   ```

7. Pull the required Ollama models:
   ```
   ollama pull llama3
   ollama pull nomic-embed-text
   ```

## Running the Application

Start the application using Streamlit:

```
streamlit run bot.py
```

The application will be available at `http://localhost:8501/`.

## PDF Processor Tool

The project includes a PDF processor tool. To use it:

```python
import os
import tools.file_processor as fp

folder_path = '/path/to/your/folder'  # Replace with the correct folder path

fp.process(folder_path)

print(f"Files processed and saved to {folder_path}")
```
