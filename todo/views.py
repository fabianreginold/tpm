from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todoItem

def todoView(request):
    all_todo_items=todoItem.objects.all()
    return render(request, 'index1.html', {'all_items':all_todo_items})
# Create your views here., 

def addTodo(request):

    new_item=todoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete=todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def but(request):
    new_item1=todoItem(content=request.POST['id'])
    new_item1.save()
    new_item2=todoItem(content=request.POST['email'])
    new_item2.save()
    new_item3=todoItem(content=request.POST['phone'])
    new_item3.save()
    new_item4=todoItem(content=request.POST['message'])
    new_item4.save()
    print(new_item1.content,new_item2.content,new_item3.content,new_item4.content)
    return HttpResponseRedirect('/todo/')


