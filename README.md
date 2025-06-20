# LocalAI Chat

A privacy-preserving chatbot that runs multiple LLM models (LLaVA, Mistral, Gemma) locally via Ollama. Features include:

- 🛡️ 100% offline operation - no data leaves your machine
- 🔄 Switch between different AI models seamlessly
- 📝 Persistent conversation memory with JSON storage
- ⚡ Real-time streaming responses
- 🖥️ Simple Gradio web interface

Perfect for developers, researchers, and privacy-conscious users who want to experiment with local LLMs without cloud dependencies.

![Demo Screenshot](screenshot.png) *(Add screenshot later)*


## Quick Start

1. Install Ollama: https://ollama.ai/
```bash
ollama pull llava:7b
ollama pull mistral:7b
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python app.py
```

4. Access at `http://localhost:7860`
