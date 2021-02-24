from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('*** 여기는 시작페이지 입니다 ***')
    context = {'ment' : '죄송합니다 어려워서요 ㅠ'}
    return render(request , 'hello/index.html', context)

def baseball(request):
    return HttpResponse("여기는 야구 입니다")

def football(request):
    return HttpResponse("여기는 축구 입니다")

def basketball(request):
    return HttpResponse("여기는 농구 입니다")

def login(request):
    msg = request.POST['msg']
    print('param msg - ', msg)
    return HttpResponse('*** 여기는 login 입니다 ***')

 # render : responce를 하는것
 # ment는 파이썬의 print