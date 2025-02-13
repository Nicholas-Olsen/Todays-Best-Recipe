import openai
import os

# 🔹 OpenAI API 키 설정 (환경 변수에서 가져오기)
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("환경 변수에 'OPENAI_API_KEY'를 설정하세요.")

# 🔹 OpenAI 클라이언트 생성
client = openai.Client(api_key=api_key)


def get_recipe(ingredients):
    """
    입력된 재료를 기반으로 요리를 추천하고 해당 요리의 종류 및 레시피를 반환하는 함수
    """
    prompt = f"""
    사용자가 입력한 재료를 바탕으로 가장 적절한 요리 종류(한식, 중식, 일식, 양식 등)를 결정하고, 그에 맞는 요리를 추천해줘.
    그리고 추천된 요리의 레시피를 단계별로 설명해줘.

    입력된 재료: {ingredients}

    출력 형식:
    - 요리 종류: [한식, 중식, 일식, 양식 중 하나]
    - 추천 요리 이름: [요리 이름]
    - 레시피:
      1. [단계 1]
      2. [단계 2]
      3. [단계 3]
    """

    # 🔹 GPT API 호출
    response = client.chat.completions.create(
        model="gpt-4o mini",  # 또는 "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )

    # 🔹 응답 데이터에서 레시피 내용 추출
    return response.choices[0].message.content


# 🔹 사용자 입력 (쉼표로 구분하여 재료 입력)
ingredients = input("사용할 재료를 입력하세요 (쉼표로 구분): ")

# 🔹 GPT API 호출하여 요리 및 레시피 받기
recipe = get_recipe(ingredients)

# 🔹 결과 출력
print("\n✨ 추천 요리 및 레시피 ✨")
print(recipe)