import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# OpenAI API 클라이언트 생성
client = openai.OpenAI(api_key="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")

def chat_gpt(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150
            )
            gpt_response = response.choices[0].message.content  # 최신 방식으로 응답 받기
        except Exception as e:
            gpt_response = f"Error: {str(e)}"

        return JsonResponse({"user_input": user_input, "response": gpt_response})

    return render(request, "gpt.html")
