# LocalAI Chat

A privacy-preserving chatbot that runs multiple LLM models (LLaVA, Mistral, Gemma) locally via Ollama. Features include:

- 🛡️ 100% offline operation - no data leaves your machine
- 🔄 Switch between different AI models seamlessly
- 📝 Persistent conversation memory with JSON storage
- ⚡ Real-time streaming responses
- 🖥️ Simple Gradio web interface

Ideal for developers, researchers, and privacy-conscious users who want to experiment with local large language models (LLMs) without relying on cloud dependencies.

![image](https://github.com/user-attachments/assets/d0bd0f83-c85e-4386-9e65-a19051778b0f)



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
