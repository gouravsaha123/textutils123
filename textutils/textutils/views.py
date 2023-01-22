from django.http import HttpResponse
from django.shortcuts import render

def removepunc(t):
    puncs = '''"'/><;:@#%^&*()\|?{}[]+-,.=`~‘’'''
    rt = ''
    for i in t:
        if i not in puncs:
            rt += i
    return rt
def removen(t):
    rt = ''
    for i in t:
        if i!='\n' and i!='\r':
            rt += i
    return rt
def removes(string):
    return string.replace(" ", "")



def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("<>about</h1>")
    params = {'name':'Harry','place':'Mars'}
    return render(request,'about.html',params)

def analyse(request):
    ptext = request.POST.get('text','default')
    ucb=''
    v1 = request.POST.get('removepunc','Off')
    v2 = request.POST.get('Fully Capitalized','Off')
    v3 = request.POST.get('Space Remover','Off')
    v4 = request.POST.get('new line Remover', 'Off')
    if v1=='on':
        ucb+='-> Removed Puncuation\n'
        ptext = removepunc(ptext)
    if v2=='on':
        ucb+='-> Fully Capitalized\n'
        ptext = ptext.upper()
    if v3=='on':
        ucb+='-> Space Remover\n'
        ptext =removes(ptext)
    if v4=='on':
        ucb += '-> new line Remover\n'
        ptext =removen(ptext)
    
    params = {'ptext':ptext,'used_ch_box':ucb}
    return render(request,'analyse.html',params)