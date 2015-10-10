from django.shortcuts import render

def hello2(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)