from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


def logout_request(request):
    logout(request)
    return redirect('store:store')

def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            request.session['customer'] = user.id
            login(request, user)
            return redirect('store:store')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'user_login_bootstrap.html', context)
    else:
        return render(request, 'user_login_bootstrap.html', context)
