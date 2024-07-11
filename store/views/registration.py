from django.contrib.auth import login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

import logging

from store.models.customer import Customer

# Get an instance of a logger
logger = logging.getLogger(__name__)


def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']

        # check user exist
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, password=password)
            Customer.objects.create(user=user, first_name=firstname, last_name=lastname,
                                    email=email, phone=phone)
            login(request, user)
            return redirect('store:store')
        else:
            context['message'] = "User already exist."
            return render(request, 'user_registration_bootstrap.html', context)
