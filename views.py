from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from django.shortcuts import redirect

@login_required
def home(request):
    context = {
        'tasks': Task.objects.all().filter(receiver = request.user),
        'username': request.user.username,
    }
    return render(request, 'website/home.html', context)

@login_required
def delete(request, id):

    Task.objects.filter(receiver = request.user)
    Task.objects.filter(id = id).delete()

    return redirect('website-home')
