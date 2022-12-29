from django.db import models

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey('accounts.user', on_delete=models.CASCADE, blank=True) # 작성자
    category = models.BooleanField() # 수입, 지출 구분
    amount_moved = models.IntegerField() # 금액
    memo = models.CharField(max_length=100) # 내용
    created_at = models.DateTimeField('생성시간', auto_now_add=True) # 생성 시간
    updated_at = models.DateTimeField('수정시간', auto_now=True) # 마지막 수정 시간
    class Meta:
        ordering = ['-id'] # 최신순으로 보이도록