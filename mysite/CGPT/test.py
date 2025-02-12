import requests
# GPT-4 API URL
GPT_API_URL = "https://api.openai.com/v1/chat/completions"  # 최신 엔드포인트
# GPT API 키
GPT_API_KEY = "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"  # 실제 API 키로 교체하세요
def get_gpt_response(prompt):
    """
    GPT-4와 통신하여 응답을 받음
    """
    headers = {
        "Authorization": f"Bearer {GPT_API_KEY}",
        "Content-Type": "application/json",
    }
    # 요청 데이터
    data = {
        "model": "gpt-3.5-turbo",  # 사용 가능한 모델명으로 변경
        "messages": [
            {"role": "user", "content": "한식 메뉴 3가지 알려줘"}  # 사용자 메시지
        ],
        "max_tokens": 150,
    }
    response = requests.post(GPT_API_URL, headers=headers, json=data)
    # 응답 확인
    response.raise_for_status()  # 에러 발생 시 예외 던짐
    return response.json()["choices"][0]["message"]["content"].strip()