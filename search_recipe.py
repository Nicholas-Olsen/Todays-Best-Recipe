import requests

# API 키 설정 (여기서 'YOUR_API_KEY'는 실제 API 키로 교체하세요)
api_key = "1efcf639a8ef4830b13e5c6747dd8948"

# Spoonacular API URL
search_url = "https://api.spoonacular.com/recipes/complexSearch"
info_url = "https://api.spoonacular.com/recipes/{}/information"  # 레시피 정보 URL (레시피 ID 포함)

# 사용자로부터 재료 입력 받기
ingredients = input("레시피에 사용될 재료를 입력하세요 (쉼표로 구분): ")

# 요청 파라미터 설정
params = {
    'query': ingredients,  # 사용자가 입력한 재료
    'number': 5,           # 검색할 레시피 수
    'apiKey': api_key      # API 키
}

# 레시피 검색 API 호출
response = requests.get(search_url, params=params)

# 응답 처리
if response.status_code == 200:
    data = response.json()  # JSON 응답을 Python 딕셔너리로 변환
    if data['results']:
        print(f"'{ingredients}' 재료로 찾은 레시피:")
        for recipe in data['results']:
            # 각 레시피의 ID
            recipe_id = recipe['id']
            
            # 레시피 상세 정보 요청
            info_response = requests.get(info_url.format(recipe_id), params={'apiKey': api_key})
            
            if info_response.status_code == 200:
                recipe_details = info_response.json()
                
                # 레시피 제목과 이미지 출력
                print(f"\nTitle: {recipe_details['title']}")
                print(f"Image: {recipe_details['image']}")
                
                # 레시피 재료 출력
                print("\nIngredients:")
                for ingredient in recipe_details['extendedIngredients']:
                    print(f"- {ingredient['original']}")
                
                # 레시피 요리 방법 출력
                print(f"\nInstructions:\n{recipe_details['instructions']}")
            else:
                print(f"레시피 상세 정보 요청 실패. 상태 코드: {info_response.status_code}")
            
            print('-' * 50)
    else:
        print(f"'{ingredients}' 재료로 찾을 수 있는 레시피가 없습니다.")
else:
    print(f"API 호출 실패. 상태 코드: {response.status_code}")
