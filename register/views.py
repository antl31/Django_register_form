from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterForm

# Create your views here.


def new_post(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        print('data')

        return HttpResponse('Спасибо за Регистрацию!')

    return render(request, 'post.html', {'form': form})
