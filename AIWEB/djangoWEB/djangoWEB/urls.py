"""djangoWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://localhost:8000/hello/
    path('hello/', include('HelloApp.urls')) ,
]

#include() 함수는 다른 URLconf들을 참조할 수 있도록 도와줍니다
# 언제 include()를 사용해야 하나요?
# 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 합니다. admin.site.urls가 유일한 예외입니다.