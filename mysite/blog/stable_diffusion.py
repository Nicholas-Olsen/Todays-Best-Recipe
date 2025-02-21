import os
import torch
from PIL import Image
from diffusers import StableDiffusionPipeline

# Stable Diffusion 모델 로드
MODEL_PATH = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(MODEL_PATH)
pipe.to(device)

# 이미지 저장 폴더 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 경로
STATIC_IMAGE_PATH = os.path.join(BASE_DIR, "..", "blog", "static", "generated")
# os.makedirs(STATIC_IMAGE_PATH, exist_ok=True)

# 음식 관련 키워드 리스트
FOOD_KEYWORDS = {
    "비빔면": "A close-up of a steaming hot Korean spicy cold noodles (비빔면) served in a white ceramic bowl, garnished with sesame seeds and green onions, high-quality, realistic lighting",
    "김치볶음밥": "A top-down view of a sizzling hot plate of Korean kimchi fried rice (김치볶음밥) with a fried egg on top, served in a black stone bowl, ultra-detailed, realistic lighting",
    "짜장면": "A high-resolution photo of delicious Korean-Chinese black bean noodles (짜장면) with rich, glossy black sauce, chopped pork, and fresh cucumbers, served in a deep ceramic bowl",
    "짬뽕": "A steaming hot bowl of spicy Korean-Chinese seafood noodle soup (짬뽕), filled with shrimp, mussels, squid, and vegetables, served in a deep red broth, high-quality, ultra-detailed",
    "부대찌개": "A hearty pot of Korean army stew (부대찌개) with bubbling red broth, sausages, spam, tofu, and instant noodles, served in a large metal pot, realistic lighting, ultra-detailed",
    "감자양파전": "A crispy Korean-style potato and onion pancake (감자양파전), golden brown and served on a wooden plate, garnished with chopped green onions, realistic food photography",
    "김치찌개": "A close-up of Korean kimchi stew (김치찌개) with soft tofu, pork, and fermented kimchi in a spicy red broth, served in a traditional black earthenware pot, ultra-detailed",
    "감자 조림": "A glossy and delicious Korean soy-braised potatoes (감자 조림), small baby potatoes coated in a rich soy glaze, garnished with sesame seeds and green onions",
    
}

def is_food_prompt(prompt: str) -> bool:
    """입력된 프롬프트가 음식 관련 키워드를 포함하는지 확인"""
    prompt_lower = prompt.lower()
    return any(keyword in prompt_lower for keyword in FOOD_KEYWORDS)

def generate_image(prompt: str):
    """Stable Diffusion을 실행하여 음식 이미지를 생성하고 저장하여 URL 반환"""
    print(f"🔹 Stable Diffusion 실행: {prompt}")

    # 음식 키워드 필터링
    if not is_food_prompt(prompt):
        print("음식과 관련된 이미지만 생성할 수 있습니다.")
        return None  # 음식이 아닌 경우 이미지 생성 안 함
    
    promptgen = ""
    
    if prompt in FOOD_KEYWORDS:
        promptgen = FOOD_KEYWORDS[prompt]
    else:
        # ✅ 기본적인 음식 스타일을 추가
        promptgen = f"A high-quality, realistic photo of {prompt} plated on a table, ultra-detailed, realistic lighting"

    print(f"📌 최종 프롬프트: {promptgen}")


    # 이미지 생성 시도
    try:
        # image = pipe(f"high-quality, realistic photo of {promptgen} plated on a table").images[0]
        image = pipe(promptgen).images[0]
        print("이미지 생성 완료")
    except Exception as e:
        print(f"Stable Diffusion 오류 발생: {e}")
        return None  # 오류 발생 시 None 반환

    # 이미지 파일명 설정 (공백 제거)
    image_filename = f"{prompt.replace(', ', '_').replace(' ', '')}.png"
    image_path = os.path.join(STATIC_IMAGE_PATH, image_filename)
    image_url = f"{image_filename}"
    print(f" 저장될 이미지 경로: {image_path}")  

    # 이미지 저장
    try:
        image.save(image_path)
        print(f"이미지 저장 완료: {image_path}")
    except Exception as e:
        print(f"이미지 저장 오류: {e}")
        return None  # 저장 실패 시 None 반환

    return image_url  # 웹에서 접근 가능한 URL 반환
