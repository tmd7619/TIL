from django.http import JsonResponse
from django.shortcuts import render , redirect

from .models import *
import csv
# Create your views here.

# select * from table;
# -> modelName.objects.all()

# select * from table where id = xxxx;
# -> modelName.objects.get(id = xxxx)
# -> modelName.objects.filter(id = xxxx)

# select * from table where id = xxxx and pwd = xxxx;
# -> modelName.objects.get(id = xxxx, pwd = xxxx)
# -> modelName.objects.filter(id = xxxx, pwd = xxxx)

# select * from table where id = xxxx or pwd = xxxx;
# -> modelName.objects.filter(Q(id = xxxx) | Q(pwd = xxxx))

# select * from table where subject like '%공지%'
# -> modelName.objects.filter(subject__icnotains='공지')
# select * from table where subject like '%공지%'
# -> modelName.objects.filter(subject__startswith='공지')
# select * from table where subject like '%공지'
# -> modelName.objects.filter(subject__endswith='공지')

# insert into table values()
# model(attr=value, attr=value)
# model.save()

# delete * from tableName where id = xxxx
# -> modelName.objects.get(id=xxx).delete()

# update tableName set attr = value where id = xxxx
# obj = modelName.objects.get(id=xxxxx)
# obj.attr = value
# obj.save() -- commit

def index(request) :   # 로그인된 상태에서, index로 갔을때 index창(로그인창)이 아닌 home으로 가게 설정함
    if request.session.get('user_id') and request.session.get('user_name') :
        context = {'id' : request.session['user_id'], # session을 여러 페이지에 활용하러면 context에 심어주는 설정을 해줘야함
                   'name' : request.session['user_name']}
        return render(request, 'home.html', context)
    else :

        return render(request, 'login.html')

# 사용자의 상태정보 저장을 위해서는 session, cookie
def logout(request) :
    request.session['user_name']    = {} # 세션을 변경시키다 = 세션 날리다
    request.session['user_id']      = {}
    request.modified                = True  # 세션 변경을 해주는 commit 명령어
    return redirect('index') # url이 logout으로 납두는게 아니라, 로그인창(index)로 가야하기 때문에 redirect

def loginProc(request) :
    print('request - loginProc')
    if request.method == 'GET' :
        return redirect('index')
    elif request.method == 'POST' :
        id = request.POST['id']
        pwd = request.POST['pwd']
        # select * from bbsuserregister where user_id = id and user_pwd = pwd
        # orm class - table
        user = BbsUserRegister.objects.get(user_id = id , user_pwd=pwd)
        print('user result - ', user) # objects = select , get~ = where 절, Bbs ~ = from bbbs~
        context = {} # context 생성
        if user is not None   :
            request.session['user_name'] = user.user_name # session create 데이터를 저장하기 위해
            request.session['user_id'] = user.user_id # session create
            context['name'] = request.session['user_name']
            context['id'] = request.session['user_id']
            return render(request, 'home.html', context) # 만든 context를 home.html에서 적용될 수 있도록 렌더링
        else :
            return redirect('index')

def registerForm(request) :
    print('request - registerForm')
    return render(request, 'join.html')

def register(request) :
    # id, pwd, name -> model -> db(insert)
    if request.method == 'POST' :
        id      = request.POST['id']
        pwd     = request.POST['pwd']
        name    = request.POST['name']
        register = BbsUserRegister(user_id = id , user_pwd = pwd, user_name = name)
        register.save()
    return render(request, 'login.html')

# bbs

def bbs_list(request) :
    # select * from bbs ;
    # modelName.objects.all()
    boards = Bbs.objects.all()
    print('bbs)list request - ', type(boards), boards)  #모델에서 데이터 가져옴
    context = {'boards' : boards , # 템플릿으로 보내는 과정
               'name'   : request.session['user_name'],
               'id'     : request.session['user_id']}
    return render(request, 'list.html', context) # list.html 에 context 를 포함하여 rendering

def bbs_registerForm(request):
    print('request bbs_registerForm - ')
    context = {'name': request.session['user_name'],
               'id': request.session['user_id']}
    return render(request, 'bbsRegisterForm.html', context)


def bbs_register(request):
    title   = request.POST['title']
    writer  = request.POST['writer']
    content = request.POST['content']
    print('request bbs_register - ', title , content, writer)
    # inser into table values(title, writer, content)
    board = Bbs(title=title, writer=writer, content=content)
    board.save()
    return redirect('bbs_list') # render 대신 redirect


def bbs_read(request , id): # get방식은 인자 두개 받아야함 urls에서 <int:id>
    print('request bbs_read param id - ' , id)
    # select * from bbs where id = id
    board = Bbs.objects.get(id = id)
    # update table set viewcnt = viewcnt + 1 value where id = id
    board.viewcnt = board.viewcnt + 1
    board.save()
    print('request bbs_read result - ', board)
    context = {'boardapp' : board ,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }
    return render(request, 'read.html', context)

def bbs_remove(request):
    id = request.POST['id']
    print('request bbs_remove param - ', id)
    Bbs.objects.get(id=id).delete()
    return redirect('bbs_list')


def bbs_modifyForm(request):
    id = request.POST['id']
    print('request bbs_remove param - ', id)
    board = Bbs.objects.get(id=id) # 빨간 id는 모델의 자동으로 생성된 기본키
    context = {'boardapp': board,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }

    return render(request, 'modify.html', context)

def bbs_modify(request) :
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    print('request bbs_modify param - ', id, title, content, writer)
    board = Bbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save()
    return redirect('bbs_list')

def bbs_search(request):
    type = request.POST['type'] # title, writer
    keyword = request.POST['keyword']
    print('request bbs_search - ' ,type, keyword)

    # select * from table where title like '%공지%'
    # select * from table where writer like '%공지%'

    # ary = -> modelName.objects.filter(TYPE__icontains='KEYWORD')
    # list [{} , {}]
    if type == 'title' :
        boards = Bbs.objects.filter(title__icontains = keyword)
    if type == 'writer' :
        boards = Bbs.objects.filter(writer__startswith= keyword)
    list = []
    for board in boards :
        list.append({
            'id' : board.id , 'title' : board.title, 'writer' : board.writer,
            'regdate' : board.regdate, 'viewcnt' : board.viewcnt
        })
    return JsonResponse(list, safe=False)

def csvUpload(request):
    file = request.FILES['csv_file']
    print('request upload - ', file)
    if not file.name.endswith('.csv'):
        return redirect('index')

    result_file = file.read().decode('utf-8').splitlines()
    print('result_file', result_file , type(result_file))

    reader = csv.reader(result_file)
    list = []
    for row in reader :
        print('row - ', row)
       # list.append(csvModel(name=row[0],img=row[1],statut=row[2]))
        file.close()
        # csvModel.objects.bulk.create(list)
        return redirect('index')
