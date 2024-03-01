from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView
from .models import User
from .models import GoodJobMsg
from .forms import GoodJobForm
import datetime
#import cv2
import base64
from django.db.models import Count
#import numpy as np
#import io

def index(request):
    params = {
                'title': 'GoodJob入力',         
            }
    return render(request, 'hello/index.html', params)


def cardWrite(request):
    userList = User.objects.all()
    params = {
                'title': 'GoodJob入力',
                'message':'フォームを記入して、カードを作成します。',
                #'form':GoodJobForm(),
                'userList':userList,            
            }
    return render(request, 'hello/card.html', params)

def cardView(request):
    fromPerson = request.POST['frPerson']
    toPerson = request.POST['toPerson']
    msg = request.POST['message']
    cardpath = request.POST['cardpath']
    params = {
                'title': 'GoodJob Card 入力',
                'fromPerson': fromPerson,
                'toPerson': toPerson,
                'message':msg,
                'cardpath':cardpath,
            }
    return render(request, 'hello/cardview.html', params)

def regist(request):
    if (request.method == 'POST'):    
        fromPerson = request.POST['frPerson']
        toPerson = request.POST['toPerson']
        msg = request.POST['message']
        cardpath = request.POST['cardpath']
        today = datetime.date.today()
        #cardDataFull = request.POST['carddata']
        #cardData = cardDataFull[22:]
        #recordNum = GoodJobMsg.objects.all().count()
        #cardName = str(recordNum) + '.png'
        #outfile_path = 'hello/static/hello/savedcard/' + cardName
        #with open(outfile_path, "wb") as f:
        #    f.write(base64.b64decode(cardData))
        #savedCardPath = '/static/hello/savedcard/' + cardName
        #print(cardData)
        
        goodJobMsg = GoodJobMsg(date=today,frName=fromPerson,toName=toPerson,message=msg,cardpath=cardpath)
        goodJobMsg.save()
        
        params = {
                    'title': 'GoodJob Card 入力',
                    'fromPerson': fromPerson,
                    'toPerson': toPerson,
                    'message':msg,
                    'cardpath':cardpath,
                    'date':today,                
                }
        return render(request, 'hello/regist.html', params)
    else:
        params = {
            'title': 'GoodJob入力',         
        }
        return render(request, 'hello/index.html', params)

def cardShow(request):
    today = datetime.date.today()
    thisMonthFirstDay = today.replace(day=1)
    cardList = GoodJobMsg.objects.filter(date__gte=thisMonthFirstDay,date__lte=today)
    #cardList = GoodJobMsg.objects.all()
    params = {
                'title': 'GoodJob入力',
                'message':'フォームを記入し、送信ボタンを押してください。',
                'today':today,
                'cardList':cardList,            
            }
    return render(request, 'hello/cardshow.html', params)

def result(request):
    today = datetime.date.today()
    thisMonthFirstDay = today.replace(day=1)
    #sql = 'select toName, count(toName) as pt from hello_GoodJobMsg where date between ' + thisMonthFirstDay + ' and ' + today + 'group by toName order by pt'
    cardList = GoodJobMsg.objects.filter(date__gte=thisMonthFirstDay,date__lte=today)
    rankingList = cardList.values('toName').annotate(total=Count('toName')).order_by('-total') 
    firstRec = cardList.values('toName').annotate(total=Count('toName')).order_by('-total').first()
    #cardList = GoodJobMsg.objects.all()
    params = {
                'title': 'GoodJob入力',
                'today':today,
                'rankingList':rankingList,  
                'firstRec':firstRec,
            }
    return render(request, 'hello/result.html', params)

#Classを利用したview
'''class HelloView(TemplateView):
    def __init__(self):
        self.params = {
                'title': 'Hello',
                'message':'your data:',
                'form':HelloForm()
                }
        
    def get(self,request):
        return render(request,'hello/index.html',self.params)
    
    def post(self,request):
        msg = '名前:' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢:' + request.POST['age']
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request,'hello/index.html',self.params)
'''        

#メソッドを利用したview
'''def index(request):
  #  if 'msg' in request.GET:
  #      msg = request.GET['msg']
  #      result = 'request parameter is ' + msg
  #  else:
  #      result = 'request parameter is null'
  #  return HttpResponse(result)
  params = {
          'title': 'Hello',
          'message':'your data:',
          'goto':'index',
          'form':HelloForm()
          }
  if (request.method == 'POST'):
      params['message'] = '名前:' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢:' + request.POST['age']
      params['form'] = HelloForm(request.POST)
  return render(request,'hello/index.html',params)


'''
'''def form(request):
    if 'msg' in request.POST:
        msg = request.POST['msg']
    else:
        msg = "名無し"

    params = {
          'title': 'index.html',
          'msg':'こんにちは' + msg + 'さん。', 
          'goto':'index'
            }
    return render(request,'hello/index.html',params)


def next(request):
  params = {
          'title': 'next.html',
          'msg':'next.htmlですよ',
          'goto':'index'
          }
  return render(request,'hello/index.html',params)
'''
    
