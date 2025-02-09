import gradio as gr
import google.generativeai as genai


genai.configure(api_key="AIzaSyD_hp5WyLzhGLUDIV7H8pIqqAbnGM4nlU4")
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
chat = model.start_chat(history=[])



def chat_with_gemini(message, history):
    history = history or []
    response = chat.send_message(message)
    history.append(("🧑 You: " + message, "🤖 : " + response.text.strip()))
    return history, history,""



with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 The Ultimate Chatbot  
    Welcome! Lets have some Chit Chat.
    """)

    chatbot = gr.Chatbot(label="Chat", bubble_full_width=False)
    msg = gr.Textbox(placeholder="Type your message...", show_label=False)
    clear = gr.Button("🧹 Clear Chat")

    state = gr.State([])

    msg.submit(chat_with_gemini, [msg, state], [chatbot, state, msg])
    clear.click(lambda: ([], []), None, [chatbot, state])

# 🚀 Launch
demo.launch()
