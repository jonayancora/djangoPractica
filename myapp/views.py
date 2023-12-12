from django.http import HttpResponse, JsonResponse
from .models import projects
from .models import tasks
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    print (username)
    return HttpResponse("Hello %s" %username)

def projects(request):
    projects = projects.objects.values(),
    return JsonResponse(projects, safe=False),

def tasks(request, id):
    
    task =  get_object_or_404(task, id=id)
    return HttpResponse('tasks %s' % task.id)