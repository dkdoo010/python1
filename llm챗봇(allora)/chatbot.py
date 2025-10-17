import gradio as gr
import subprocess

# Ollama 명령어를 통해 모델과 대화
def chat_with_ollama(history):
    # 대화 내용을 하나의 프롬프트로 구성
    prompt = ""
    for user, bot in history:
        prompt += f"User: {user}\nAssistant: {bot}\n"
    prompt += f"User: {history[-1][0]}\nAssistant:"

    # Ollama 명령어 실행
    result = subprocess.run(
        ["ollama", "run", "qwen3:1.7b"],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

    response = result.stdout.decode("utf-8").strip()
    return response

# Gradio 인터페이스 함수
def respond(message, history):
    history = history or []
    history.append((message, ""))
    response = chat_with_ollama(history)
    history[-1] = (message, response)
    return history, history

# Gradio UI 구성
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 Qwen3 챗봇 (Ollama 기반)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="메시지를 입력하세요")
    clear = gr.Button("초기화")

    state = gr.State([])

    msg.submit(respond, [msg, state], [chatbot, state])
    clear.click(lambda: [], None, chatbot)

demo.launch()
