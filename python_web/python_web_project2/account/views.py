from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 아래는 회원가입 완료 후 자동으로 로그인이 되게 하는 코드
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

# Create your views here.
