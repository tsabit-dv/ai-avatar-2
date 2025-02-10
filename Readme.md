# FastAPI AI Chatbot with Ollama Integration (Gemma 2b, M,14MS Before RAG)

## Overview
This project is a FastAPI-based chatbot that integrates AI models using Ollama. It processes user input through NLP before invoking an AI model, ensuring efficient responses. The chatbot supports various AI models, depending on your hardware capabilities, especially GPU performance.

## Installation
### Prerequisites
- Python 3.10+
- Virtual Environment (optional but recommended)
- Ollama installed ([Get Ollama](https://ollama.ai))
- Required Python packages

### Setup Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/ai-avatar-2
   cd ai-avatar-2
   ```

2. **Create and Activate Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```


4. **Run the Web on Xampp**
   ```bash
   https://localhost/step-2-aiavatar/static/
   ```

## Configuration
- **AI Model Selection**: Modify the model in `app.py` based on your hardware:
  ```python
  model = OllamaLLM(model="llama3.2:1b")  # Example model
  ```
  If your GPU supports larger models, you can load:
  ```python
  model = OllamaLLM(model="llama3:8b")
  ```
- **Timeout Limitation**: The chatbot response time is limited to **5 seconds** for better efficiency.

## Usage
- Access the API via `http://localhost:5000/chat`
- Send a POST request with JSON payload:
  ```json
  {
    "message": "Hello, how does AI work?"
  }
  ```

## Next Steps
### Implementing RAG (Retrieval-Augmented Generation)
- Integrate external knowledge sources to improve response relevance.
- Use vector databases like FAISS or ChromaDB for efficient retrieval.

### Fine-Tuning AI Models
- Train custom datasets to improve AI performance for specific use cases.
- Use tools like Hugging Face Trainer or OpenAI fine-tuning API.

## Troubleshooting
- **Slow AI response?** Ensure your GPU supports the selected model.
- **Import errors?** Check `pip list` for missing dependencies.
- **Ollama not responding?** Restart the Ollama server and reload the model.

## License
This project is open-source and available under the MIT License.

