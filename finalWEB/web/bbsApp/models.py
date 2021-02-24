from django.db import models
from django.utils import timezone
# Create your models here.

class BbsUserRegister(models.Model):  # models에 있는 Model 객체 상속
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

class Bbs(models.Model) :
    title = models.CharField(max_length=100) # Char는 한줄로 입력받음
    writer = models.CharField(max_length=100)
    content = models.TextField() # Text는 개행으로 입력받음
    regdate = models.DateTimeField (default=timezone.now()) # 값이 들어오지 않으면, default값이 assing 됨
    viewcnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title+", "+self.writer   # debug코드



# orm을 할 수 있는 테이블을 형성해주는 것 = class 생성
# 기본키 생성은 클래서 생성 시, 자동으로 부여됨
