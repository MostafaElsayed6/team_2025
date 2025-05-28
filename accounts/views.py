# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'تم إنشاء حسابك بنجاح! يمكنك تسجيل الدخول الآن.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/password.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/trips/')  # غير 'home' لاسم URL الرئيسي الخاص بك
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة!')
    return render(request, 'accounts/password.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # توجيه إلى الصفحة الرئيسية بعد تسجيل الخروج