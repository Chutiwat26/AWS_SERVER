from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee_data.models import CompanyPosition, EmployeeProfile, ProfilePosition
from customer_section.models import *
from .models import *
from django.contrib.auth.models import User
import numpy as np
from django.http import JsonResponse

# Create your views here.

@login_required
def AddCustomer(request): #Ajax
    context = {}
    login_user_position_list = []
    login_user = request.user
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    all_position = CompanyPosition.objects.all()
    all_customer = Customers.objects.all()
    all_employee = User.objects.all()
    all_profile_position = ProfilePosition.objects.all().order_by('profile_id')
    context['all_position'] = all_position
    context['all_customer'] = all_customer
    context['all_employee'] = all_employee
    context['all_profile_position'] = all_profile_position
    admin_status = False
    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        login_user_position_list = np.append(login_user_position_list,login_user_position.position_name)
        if login_user_position.position_name =='purchasing' :
            	purchasing_status = True

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
    
    if 	purchasing_status:
        if request.method == "POST":
            data = request.POST.copy()
            if str(data.get('add_customer')) == '':
                customer_full_name = data.get('new_customer_full_name')
                customer_initial_name = data.get('new_customer_initial_name')
                customer_address = data.get('new_customer_address')
                customer_tel = data.get('new_customer_tel')
                customer_email = data.get('new_customer_email')
                check_customer_1 = Customers.objects.filter(full_name = customer_full_name)
                check_customer_2 = Customers.objects.filter(initial_name = customer_initial_name)
                if len(check_customer_1) == 0 and len(check_customer_2) == 0 and len(customer_full_name) != 0 and len(customer_initial_name) != 0 :
                    customer = Customers()
                    customer.full_name = customer_full_name
                    customer.initial_name = customer_initial_name
                    customer.address = customer_address
                    customer.telephone = customer_tel
                    customer.email = customer_email
                    customer.save()
                else:
                    context['add_customer_warning_msg'] = 'Invalid customer detail'

                return JsonResponse(context)
        else:
            return render(request, 'purchase_section/purchase_add_customer.html', context)
    else:
        return redirect('/')
