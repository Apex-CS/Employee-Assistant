# Employee-Assistant | Neo4j-backed Chatbot using Python

This repository follows the "Build a Neo4j-backed Chatbot using Python" course on [Neo4j GraphAcademy](https://graphacademy.neo4j.com/).

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Git
- [Ollama](https://ollama.com/)
- A Google account for access to Google Colab

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository:
   ```
   git clone https://github.com/Apex-CS/Employee-Assistant.git
   cd Employee-Assistant
   ```

2. Open the [`Hosting_ollama-2.ipynb`](https://apx365-my.sharepoint.com/:u:/g/personal/misanchez_apexsystems_com/Eb9Udzi42IVIl4qgwBxXO4YBJNTpdFJz-m6QOyX0mmcwlQ?e=JEHbGd) file on Google Colab.

3. Select a T4 GPU Python 3 runtime.

4. Run all cells in the notebook. At the end, you'll see two URLs. Copy the one ending with `url="....ngrok-free-app"`.

6. Open the `llm.py` file in the cloned repository and replace the URLs for `ollama_emb` and `llm` with the copied URL.

7. Install Ollama on your local machine from [ollama.com](https://ollama.com/).

8. Open a terminal and verify Ollama installation by running:
   ```
   ollama
   ```

9. Set the Ollama host environment variable:
   ```
   export OLLAMA_HOST="<URL_FROM_STEP_5>"
   ```

10. Pull the required Ollama models:
    ```
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

## Running the Application

1. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

2. Start the Streamlit app:
   ```
   streamlit run bot.py
   ```

The application will be available at `http://localhost:8501/`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.

## License

[Include license information here]