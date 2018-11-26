# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from .models import TodoItem
# Create your views here.

def todoview(request):
    all_todo_items=TodoItem.objects.all()
    all_todo_items
    return render(request,'todo.html',{'all_items':all_todo_items})

def addtodo(request):
    #create a new todoitem
    c=request.POST['content']
    new_item=TodoItem(content=c)
    new_item.save()
    return redirect('/todo/')
    #save
    #redirect
def deletetodo(request, todo_id):
    item_to_del=TodoItem.objects.get(id=todo_id)
    item_to_del.delete()
    return redirect('/todo/')
