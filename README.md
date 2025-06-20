# LocalAI Chat

A privacy-preserving chatbot that runs multiple LLM models (LLaVA, Mistral, Gemma) locally via Ollama. Features include:

- 🛡️ 100% offline operation - no data leaves your machine
- 🔄 Switch between different AI models seamlessly
- 📝 Persistent conversation memory with JSON storage
- ⚡ Real-time streaming responses
- 🖥️ Simple Gradio web interface

Perfect for developers, researchers, and privacy-conscious users who want to experiment with local LLMs without cloud dependencies.

![Demo Screenshot](![image](https://github.com/user-attachments/assets/4acfbd8f-3f5e-4bb1-a581-5c739b4f6ad1)
)

![Demo Screenshot](screenshot.png![image](https://github.com/user-attachments/assets/5aff9b12-f8db-41c3-bf40-473ae468c73a)
 ) *(Add screenshot later)*


![Demo Screenshot](![image](https://github.com/user-attachments/assets/e3de4a39-fd2d-4906-8690-9fd879c7fe48)
) 



![Demo Screenshot](screenshot.png) *(Add screenshot later)*


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
