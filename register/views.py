from django.shortcuts import render
from django.http import HttpResponse
from .form import RegisterForm, GetterForm
from .models import Register
# Create your views here.


def index(request):
    form = GetterForm(data=request.POST)
    email = 0
    if form.is_valid():
        email = form.cleaned_data['email']

    regform = Register.objects.filter(email=email)

    return render(request, "getter.html", {"regform": regform})


def new_post(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('Спасибо за Регистрацию!')

    return render(request, 'post.html', {'form': form})
