from django.shortcuts   import render
from django.http        import JsonResponse
# Create your views here.

def index(request) :
    print('request index - ')
    return render(request, 'frontDemo.html' )

def nonAjax(request) :
    print('request ajax - nonAjax')
    list = [{'id': 'multicampus04', 'pwd': 'multicampus04'},
            {'id': 'multicampus05', 'pwd': 'multicampus05'}]

    return JsonResponse(list , safe=False)
    # safe=False 는 비동기통신을 하겠다

def paramAjax(request) :
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    print('ajax param - ', id, pwd)
    list = [{'id': 'multicampus04', 'pwd': 'multicampus04'},
            {'id': 'multicampus05', 'pwd': 'multicampus05'}]

    return JsonResponse(list, safe=False)


def chart(request) :

    data = [
            [1, 1],
            [2, 11],
            [2, 2],
            [2, 2],
            [3, 2],
            [4, 7]
        ]
    context = {'data' : data }
    return render(request , 'chartDemo.html' , context)
