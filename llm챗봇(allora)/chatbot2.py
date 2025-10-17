import gradio as gr
from ollama import Client

# Ollama 로컬 서버 연결
client = Client(host='http://localhost:11434')

# 사용할 모델 이름
MODEL = 'qwen3:1.7b'

# 시스템 프롬프트 (선택사항)
SYSTEM_PROMPT = "당신은 친절한 AI 도우미입니다. 사용자의 요청을 한국어로 이해하고 대답해주세요."

# 대화 이력을 저장할 리스트
chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def generate_response(user_input, history):
    # 시스템 프롬프트는 최초에만 추가
    if not history:
        history = [{"role": "system", "content": SYSTEM_PROMPT}]
    else:
        history = history.copy()

    # 사용자 메시지 추가
    history.append({"role": "user", "content": user_input})

    # 모델 응답 생성
    response = client.chat(model=MODEL, messages=history)
    answer = response['message']['content']

    # 응답 추가
    history.append({"role": "assistant", "content": answer})

    return answer


# Gradio 인터페이스 생성 (멀티턴 지원)
chatbot = gr.ChatInterface(
    fn=generate_response,
    title="💬 Qwen3 챗봇 (로컬 LLM)",
    theme="soft",
    examples=["안녕!", "파이썬으로 웹 서버 만드는 법 알려줘", "너는 어떤 모델이야?"
              ,"오늘 날씨 알려줘", "점심 메뉴 추천해줘"],
    submit_btn="보내기",
    stop_btn="중단"
)


if __name__ == "__main__":
    chatbot.launch()