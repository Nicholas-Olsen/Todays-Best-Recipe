import requests

# API 키 설정 (여기서 'YOUR_API_KEY'는 실제 API 키로 교체하세요)
api_key = "1efcf639a8ef4830b13e5c6747dd8948"

# Spoonacular API URL
url = "https://api.spoonacular.com/recipes/findByIngredients"

# 사용자로부터 재료 입력 받기
ingredients = input("레시피에 사용될 재료를 입력하세요 (쉼표로 구분): ")

# 요청 파라미터 설정
params = {
    'ingredients': ingredients,  # 사용자가 입력한 재료
    'number': 5,                 # 검색할 레시피 수
    'apiKey': api_key            # API 키
}

# API 호출
response = requests.get(url, params=params)

# 응답 처리
if response.status_code == 200:
    data = response.json()  # JSON 응답을 Python 딕셔너리로 변환
    if data:
        print(f"'{ingredients}' 재료로 찾은 레시피:")
        for recipe in data:
            print(f"Title: {recipe['title']}")
            print(f"Image: {recipe['image']}")
            print('-' * 50)
    else:
        print(f"'{ingredients}' 재료로 찾을 수 있는 레시피가 없습니다.")
else:
    print(f"API 호출 실패. 상태 코드: {response.status_code}")
