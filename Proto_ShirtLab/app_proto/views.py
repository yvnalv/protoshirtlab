from django.shortcuts import render
from app_proto.models import SLUser,AdminUser
from app_proto.forms import UserForm, UserBaseForm,UserProfileForm
# Create your views here.

#Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'app_proto/index.html')

def sl_users(request):
    userlist = SLUser.objects.order_by('first_name')
    userdict = {'users':userlist}
    return render(request,'app_proto/user.html',context=userdict)

def signup(request):
    signed = UserForm()

    if request.method == "POST":
        signed = UserForm(request.POST)

        if signed.is_valid():
            signed.save(commit=True)
            return sl_users(request)

    return render(request,'app_proto/signup.html',{'signed':signed})

def registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserBaseForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES('profile_pics')

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserBaseForm()
        profile_form = UserProfileForm()

    return render(request,'app_proto/registration.html',{'user_form':user_form,
                                                         'profile_form':profile_form,
                                                         'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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
                return HttpResponse("Account is not active!")

        else:
            print('Someone tried to login and failed')
            print('Username : {} and password {}'.format(username,password))
            return HttpResponse('Invalid login details')
    else:
        return render(request,'app_proto/login.html',{})
