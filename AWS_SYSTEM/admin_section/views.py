from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee_data.models import CompanyPosition, EmployeeProfile, ProfilePosition
from .models import *
from django.contrib.auth.models import User
import numpy as np
# Create your views here.
@login_required
def AddAssignPosition(request):
    context = {}
    login_user_position_list = []
    login_user = request.user
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    all_position = CompanyPosition.objects.all()
    context['all_position'] = all_position
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
            add_postion = data.get('new_position')
            check_position = CompanyPosition.objects.filter(position_name=add_postion)
            if len(add_postion) and len(check_position) == 0:
                position = CompanyPosition()
                position.position_name = add_postion
                position.save()
            else:
                context['warning_msg'] = 'Invalid position name'
        return render(request, 'admin_section/add&assign-position-page.html', context)
    else:
        return redirect('/')