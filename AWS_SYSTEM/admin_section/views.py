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
def AdminPage(request): #Ajax
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
        if login_user_position.position_name == 'administration' :
            admin_status = True

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
    
    if admin_status:
        if request.method == "POST":
            data = request.POST.copy()
            if str(data.get('add_position')) == '':
                add_postion = data.get('new_position')
                check_position = CompanyPosition.objects.filter(position_name=add_postion)
                if len(add_postion) != 0 and len(check_position) == 0:
                    position = CompanyPosition()
                    position.position_name = add_postion
                    position.save()
                else:
                    context['add_position_warning_msg'] = 'Invalid position name'

                return JsonResponse(context)
            
            elif str(data.get('add_customer')) == '':
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

            elif str(data.get('assign_position')) == '':
                employee_username = data.get('admin_employee')
                selected_position = data.get('employee_position')
                try:
                    selected_employee = User.objects.get(username = employee_username)
                    employee_detail = EmployeeProfile.objects.get(user = selected_employee)
                    position_detail = CompanyPosition.objects.get(position_name = selected_position)
                    check_employee_position = ProfilePosition.objects.get(profile_id=employee_detail.pk, position_id=position_detail.pk)
                    context['assign_position_warning_msg'] = 'Invalid assigning position'
                except:
                    employee_position = ProfilePosition()
                    employee_position.profile_id = employee_detail
                    employee_position.position_id = position_detail
                    employee_position.save()

                return JsonResponse(context)

        return render(request, 'admin_section/admin-management-page.html', context)
    else:
        return redirect('/')
    '''
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
        if login_user_position.position_name == 'administration' :
            admin_status = True

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
    
    if admin_status:
        if request.method == "POST":
            data = request.POST.copy()
            if str(data.get('add_position')) == '':
                add_postion = data.get('new_position')
                check_position = CompanyPosition.objects.filter(position_name=add_postion)
                if len(add_postion) != 0 and len(check_position) == 0:
                    position = CompanyPosition()
                    position.position_name = add_postion
                    position.save()
                else:
                    context['add_position_warning_msg'] = 'Invalid position name'
            
            elif str(data.get('add_customer')) == '':
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

            elif str(data.get('assign_position')) == '':
                employee_username = data.get('admin_employee')
                selected_position = data.get('employee_position')
                selected_employee = User.objects.get(username = employee_username)
                employee_detail = EmployeeProfile.objects.get(user = selected_employee)
                position_detail = CompanyPosition.objects.get(position_name = selected_position)
                try:
                    check_employee_position = ProfilePosition.objects.get(profile_id=employee_detail.pk, position_id=position_detail.pk)
                    context['assign_position_warning_msg'] = 'Invalid assigning position'
                except:
                    employee_position = ProfilePosition()
                    employee_position.profile_id = employee_detail
                    employee_position.position_id = position_detail
                    employee_position.save()

        return render(request, 'admin_section/admin-management-page.html', context)
    else:
        return redirect('/')

    '''
