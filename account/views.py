from django.shortcuts import render
from django.views import View
from .forms import CustomUserCreationForm, CustomeErrorList
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect


class AccountView(View):
    template_name = 'account/login.html'


def register(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'account/register.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST,error_class = CustomeErrorList)
        if form.is_valid():
            form.save()
            return redirect('account.login')
        else:
            template_data['form'] = form
            return render(request, 'account/register.html',
                          {'template_data': template_data})



def login(request):
    template_data = {}
    template_data['title'] = 'Log in'
    if request.method == 'GET':
        return render(request, 'account/login.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
        return render(request, 'account/login.html',
                      {'template_data': template_data})
    else:
        auth_login(request, user)
        return redirect('home.index')