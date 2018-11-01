from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *


def index(request):

    return render(request, 'app/index.html', {})

def join(request):
    if request.method == 'GET':
        return render(request, 'app/join.html', {})

    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        m = Member(id=id, pw=pw, name=name)
        m.save()

        return render(request, 'app/join_result.html',
                      {'id':id, 'name':name})

def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass

        res = {'id':id, 'msg':'가입 가능'}
        return JsonResponse(res)
    else:
        res = {'id':id, 'msg':'가입불가'}
        return JsonResponse(res)

def login(request):
    if request.method == 'GET':

        return render(request, 'app/login.html',{})

    else:
        id = request.POST['id']
        pw = request.POST['pw']

        try:
            Member.objects.get(id=id, pw=pw)
        except Member.DoesNotExist:
            return redirect('login')

        else:
            request.session['id']=id
            return redirect('/app/index')
