# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, 'words/index.html')

def add(request):  
    if request.method == "POST":
        newWord = {}
        newWord['word'] = request.POST['word']
        newWord['color'] = request.POST['color']
        newWord['today'] = datetime.datetime.now().strftime("%I:%M %p, %b %m %Y")
        
        if "fontSize" in request.POST:
            request.session['size'] = 'big'
        else:
            request.session['size'] = 'regular'

        newWord['size'] = request.session['size']

        # temp = request.session['words']  ------- alt, without request.session.modified = True 
        # temp.append(newWord)
        # request.session['words'] = temp
        request.session['words'].append(newWord)
        request.session.modified = True
        
        return redirect(index)
    else:
        return redirect(index) 

def clear(request):
    del request.session['words']
    return redirect(index)


