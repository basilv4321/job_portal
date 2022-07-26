from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView
from users.models import User
from users.forms import UserRegistrationForm,SigninForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.

class SignupView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

class SigninView(FormView):
    model=User
    form_class = SigninForm
    template_name = 'login.html'

    def post(self,request,*args,**kwargs):
        form=SigninForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if not user:
                return render(request,'login.html',{'form':form})
            login(request,user)
            if request.user.is_candidate:
                return redirect('cand-home')
            else:
                return redirect('emp-home')

