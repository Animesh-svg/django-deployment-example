from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm       # Import from Forms.py to views.py

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#my extra creativity to retrive datas
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    #user_output = UserProfileInfo.objects
    return render(request,'basic_app/index.html')

def special(request):
    return render(request,'basic_app/special.html')
#    return HttpResponse("<h1>You are logged in, Nice</h1>")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user         # OneToOneField can be done with this line of code

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponseRedirect("Account is not active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Login Details are invalid!")
    else:
        return render(request,'basic_app/login.html',{})
