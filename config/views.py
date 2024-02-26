from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data =request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                 login(request, user)
                 return redirect('index')
           
    login_form = AuthenticationForm()    
    return render(request, 'login.html', {'form': login_form})
 
def logout_page(request):
    logout(request)
    return redirect('login')