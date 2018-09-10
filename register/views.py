
from django.shortcuts import render
from django.http import HttpResponse
from register.models import Register
import hashlib
# Create your views here.

def post(request):
    errors = []
    form = {}
    if request.POST:

        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['password'] = request.POST.get('password')
        form['message'] = request.POST.get('message')

        if not form['name']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')

        if not errors:
            reg = Register()
            reg.name = request.POST.get('name')
            reg.email = request.POST.get('email')
            reg.password = hashlib.md5(request.POST.get('email').encode('utf-8')).hexdigest()
            reg.phone = 'dfgdf'
            reg.surname = 'sd'
            reg.save()
            # ... сохранение данных в базу
            print(type(request))
            return HttpResponse('Спасибо за ваше сообщение!')

    return render(request, 'post.html', {'errors': errors, 'form': form})
