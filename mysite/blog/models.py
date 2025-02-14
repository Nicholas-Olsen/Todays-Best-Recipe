from django.db import models

class Recipe(models.Model):
    rec_id = models.BigAutoField(primary_key=True)  # 큰 범위의 자동 증가 ID
    rec_name = models.CharField(max_length=200)  # 레시피 이름
    rec_descrip = models.TextField()  # 간단한 설명
    rec_detail = models.TextField()  # 상세 레시피
    rec_img = models.URLField(max_length=500, blank=True, null=True)  # 이미지 URL (DB와 일치)
    rec_type = models.CharField(max_length=100)  # 음식 유형 (한식, 중식 등)

    def __str__(self):
        return self.rec_name  # 객체 출력 시 레시피 이름 표시
