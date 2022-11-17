from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.models import User
import numpy as np

# Create your views here.
def EmployeeHome(request):
    context = {}
    login_user_position_list=[]
    #login_data = request.POST.copy()
    #login_username = login_data.get('username')
    login_username = request.user.username
    user_detail = User.objects.get(username=login_username)
    #login_user_pk = str(user_detail.pk) + "." + user_detail.username
    #print(login_user_pk)
    employee_profile = EmployeeProfile.objects.get(user = user_detail.pk)
    position_list = ProfilePosition.objects.filter(profile_id = employee_profile.pk)
        
    for user_position in position_list:
        position_name = CompanyPosition.objects.get(pk=user_position.position_id.pk)
        login_user_position_list = np.append(login_user_position_list,position_name.position_name)
        
    #print(len(login_user_position_list))
    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
        return render(request, 'employee_data/employee_data-home.html', context)
    else:
        context['position_status'] = False
        return render(request, 'employee_data/employee_data-home.html')
    

def EmployeeLogin(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/aws-system-intranet/intranet-home/') 
        else:
            context['warning_msg'] = 'Username or passward is invalid.'
    else:
        form = AuthenticationForm()
    return render(request, 'employee_data/login-page.html', context)

def EmployeeLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def EmployeeRegister(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy() # receive data from register page
        #print(data)
        regis_firstname = data.get('firstname')
        regis_lastname = data.get('lastname')
        regis_email = data.get('email')
        regis_telephone = data.get('telephone')
        regis_username = data.get('username')
        regis_password = data.get('password')
        regis_repassword = data.get('repassword')

        if regis_password != regis_repassword:
            context['warning_msg'] = 'Password and repassword did not match.'
            context['fill_firstname'] = regis_firstname
            context['fill_lastname'] = regis_lastname
            context['fill_email'] = regis_email
            context['fill_username'] = regis_username
            context['fill_telephone'] = regis_telephone
            return render(request, 'employee_data/register-page.html', context)

        else:
            try:
                check_username = User.objects.get(username = regis_username)
                context['warning_msg'] = 'This username is already used.'
                context['fill_firstname'] = regis_firstname
                context['fill_lastname'] = regis_lastname
                context['fill_email'] = regis_email
                context['fill_username'] = regis_username
                context['fill_telephone'] = regis_telephone
                return render(request, 'employee_data/register-page.html', context)

            except:
                newuser = User()
                newuser.username = regis_username
                newuser.email = regis_email
                newuser.first_name = regis_firstname
                newuser.last_name = regis_lastname
                newuser.set_password(regis_password)
                newuser.save()

                newprofile = EmployeeProfile()
                newprofile.user = User.objects.get(username=regis_username)
                newprofile.user_telephone = regis_telephone
                newprofile.save()

                context['first_name'] = regis_firstname
                context['last_name'] = regis_lastname

                try:
                    login_user = authenticate(username=regis_username, password=regis_password)
                    login(request, login_user)
                    #print(context)
                    return redirect('/aws-system-intranet/intranet-home/', context)
                except:
                    context['warning_msg'] = 'Username or passward is invalid.'
                    return render(request, 'employee_data/login-page.html', context)
    
    return render(request, 'employee_data/register-page.html', context)





