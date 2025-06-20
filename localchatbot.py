import gradio as gr
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage
from datetime import datetime
import json


DEFAULT_MODEL = "llava:7b"
OLLAMA_URL = "http://localhost:11434"

active_sessions = {}

# Get or create a model and its memory
def load_model(model_name):
    if model_name not in active_sessions:
        chat_model = ChatOllama(model=model_name, base_url=OLLAMA_URL, streaming=True)
        memory = ConversationBufferMemory(return_messages=True)
        active_sessions[model_name] = {
            "model": chat_model,
            "memory": memory
        }
    return active_sessions[model_name]

# Chat function that streams response as the model generates it
def chat_with_model(user_msg, history, model_name):
    session = load_model(model_name)
    model = session["model"]
    memory = session["memory"]
    memory.chat_memory.add_user_message(user_msg)

    yield history + [
        {"role": "user", "content": user_msg},
        {"role": "assistant", "content": "..."}
    ], ""

    response = ""
    for chunk in model.stream([HumanMessage(content=user_msg)]):
        response += chunk.content
        yield history + [
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": response}
        ], ""

    memory.chat_memory.add_ai_message(response)

 
def save_chat(history):
    with open("chat_memory.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def load_chat():
    try:
        with open("chat_memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# UI code
with gr.Blocks(css="""
.gradio-container {max-width: 720px; margin: auto !important}
#chat-scroll {height: 450px; overflow-y: auto; display: flex; flex-direction: column-reverse; border: 1px solid #ccc; padding: 10px; border-radius: 8px;}
#input-area {position: sticky; bottom: 0; background: white; padding-top: 10px;}
""") as app:
    
    gr.Markdown("# 🧠 Chat with Multiple LLMs (Ollama-powered)")

    with gr.Row():
        model_dropdown = gr.Dropdown(
            choices=["llava:7b", "gemma3:4b", "tinyllama:latest", "mistral:7b-instruct"],
            value=DEFAULT_MODEL,
            label="Select Model"
        )

    chat_box = gr.Chatbot(label="Chat History", elem_id="chat-scroll", type="messages")
    message_input = gr.Textbox(placeholder="Type your message here...", elem_id="input-area", show_label=False)

    with gr.Row():
        send_btn = gr.Button("Send")
        clear_btn = gr.Button("Clear")

    
    chat_box.value = load_chat()

    send_btn.click(chat_with_model, [message_input, chat_box, model_dropdown], [chat_box, message_input])
    message_input.submit(chat_with_model, [message_input, chat_box, model_dropdown], [chat_box, message_input])

   
    def save_after_send(history):
        save_chat(history)
        return history

    send_btn.click(save_after_send, chat_box, chat_box)
    message_input.submit(save_after_send, chat_box, chat_box)
 
    def clear_chat():
        save_chat([])
        return []

    clear_btn.click(clear_chat, outputs=chat_box)

 
app.launch()

