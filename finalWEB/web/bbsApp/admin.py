from django.contrib import admin
from .models import *
# Register your models here.

#모델을 관리하는 admin.py

admin.site.register(BbsUserRegister)
admin.site.register(Bbs)

# admin에 모델을 등록 후 , 마이그레이션 입력