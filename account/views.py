from django.shortcuts import render
from django.views import View
from .forms import CustomUserCreationForm, CustomeErrorList
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
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'account/register.html',
                          {'template_data': template_data})


class LoginView(View):
    template_name = 'account/login.html'
    def get(self, request):
        return