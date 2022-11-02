from django.shortcuts import render, redirect
from employee_data.models import *
from django.contrib.auth.models import User
from design_section.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import numpy as np
import datetime
 
# Create your views here.
@login_required
def WorkshopHome(request):
    context = {}
    drawing_process_list = []
    drawing_qc_list = []
    login_user = request.user
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    login_position_id = ProfilePosition.objects.get(profile_id = login_profile_id)
    login_user_position = CompanyPosition.objects.get(id=login_position_id.pk)
    context['position'] = login_user_position.position_name
    drawings_process = DrawingFile.objects.filter(Q(status = 'processing') | Q(status = 'repair'))
    drawings_qc = DrawingFile.objects.filter(status = 'QC')
    if login_user_position.position_name == "technician":
        for drawing_process in drawings_process:
            job_files = JobFile.objects.filter(drawing_id = drawing_process)
            drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_process.pk)
            for job_file in job_files:
                job_id = job_file.job_id
                #print(job_id.pk)
                job_titles = JobTiltle.objects.filter(pk=job_id.pk)
                for job_title in job_titles:
                    if login_user.username == drawing_assign.receiver_username:
                        customer = Customers.objects.get(initial_name=job_title.customer)
                        user_job = UserJob.objects.get(job_id=job_title.pk)
                        draftsman_id = User.objects.get(username=user_job.user_id)

                        drawing_json={
                            "title":job_title.title,
                            "drawing_name":drawing_process.name,
                            "drawing_id":drawing_process.pk,
                            "customer":customer.initial_name,
                            "draftsman":draftsman_id.username,
                            "submit_date":job_title.submit_date,
                            "process_date":job_title.process_date,
                            "finish_date":job_title.finish_date,
                            "status":drawing_process.status,
                            "path":drawing_process.path,
                            "responsible_person":drawing_assign.receiver_username,
                        }
                        drawing_process_list = np.append(drawing_process_list,drawing_json)
                        #print(drawing_list)
                        #print(job_title.title)
        context['drawing_process_list'] = drawing_process_list
        return render(request, 'workshop_section/job_list-page.html',context)

    elif login_user_position.position_name == "quality control":
        for drawing_qc in drawings_qc:
            job_files = JobFile.objects.filter(drawing_id = drawing_qc)
            for job_file in job_files:
                job_id = job_file.job_id
                #print(job_id.pk)
                job_titles = JobTiltle.objects.filter(pk=job_id.pk)
                for job_title in job_titles:
                    customer = Customers.objects.get(initial_name=job_title.customer)
                    user_job = UserJob.objects.get(job_id=job_title.pk)
                    draftsman_id = User.objects.get(username=user_job.user_id)

                    drawing_json={
                        "title":job_title.title,
                        "drawing_name":drawing_qc.name,
                        "drawing_id":drawing_qc.pk,
                        "customer":customer.initial_name,
                        "draftsman":draftsman_id.username,
                        "submit_date":job_title.submit_date,
                        "process_date":job_title.process_date,
                        "finish_date":job_title.finish_date,
                        "status":drawing_qc.status,
                        "path":drawing_qc.path,
                    }
                    drawing_qc_list = np.append(drawing_qc_list,drawing_json)
                    #print(drawing_list)
                    #print(job_title.title)
        context['drawing_qc_list'] = drawing_qc_list
        return render(request, 'workshop_section/qc_list-page.html',context)

@login_required
def ShowDrawingDetail(request, drawing_id):
    context = {}
    picture_list=[]
    technicians=[]
    date_time = datetime.datetime.now()
    data = request.POST.copy()
    login_user = request.user
    #print('login user is '+str(login_user))
    #print(login_user.pk)
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    #print("Profile id is " + str(login_profile_id))
    login_position_id = ProfilePosition.objects.get(profile_id = login_profile_id)
    #print("Position id is " + str(login_position_id.pk))
    login_user_position = CompanyPosition.objects.get(id=login_position_id.pk)
    #print("User position is "+str(login_user_position.position_name))
    drawing_file = DrawingFile.objects.get(pk=drawing_id)
    print(drawing_file)
    job_file = JobFile.objects.get(drawing_id=drawing_file.pk)
    print(job_file.job_id)
    job_title = JobTiltle.objects.get(pk=job_file.job_id.pk)
    print(job_title)
    customer = Customers.objects.get(pk=job_title.customer.pk)
    pictures_id = JobFile.objects.filter(job_id=job_file.job_id.pk)
    #print(pictures_id)
    user_job = UserJob.objects.get(job_id=job_title.pk)
    draftsman = User.objects.get(username=user_job.user_id.username)
    draftsman_full_name = draftsman.first_name + ' ' + draftsman.last_name
    sender = login_user.username
    context['position'] = str(login_user_position.position_name)

    if request.method == "POST":
        if str(data.get('workshop_submit')) == '':
            drawing_file.status = "QC"
            drawing_file.save()

            drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_file.pk)
            drawing_assign.job_state = "QC"
            drawing_assign.save()

        elif str(data.get('reject_submit')) == '':
            drawing_file.status = "reject"
            drawing_file.save()

            drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_file.pk)
            drawing_assign.job_state = "reject"
            drawing_assign.save()

        elif str(data.get('repair_submit')) == '':
            drawing_file.status = "repair"
            drawing_file.save()

            drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_file.pk)
            drawing_assign.job_state = "repair"
            drawing_assign.save()

        elif str(data.get('accept_submit')) == '':
            drawing_file.status = "finished"
            drawing_file.save()

            drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_file.pk)
            drawing_assign.job_state = "finished"
            drawing_assign.save()

            job_title.finish_date = date_time
            job_title.save()

        return render(request, 'workshop_section/workshop_action_result-page.html' , context)
        

    try:
        drawing_detail = DrawingDetail.objects.get(drawing_id=drawing_file.pk)
        file_drawing_detail = FileDetail.objects.get(pk=drawing_detail.detail_id.pk)
        drawing_description = file_drawing_detail.detail
    except:
        drawing_description = "No drawing description."
    
    selected_drawing = {
        "title":job_title.title,
        "customer":customer.initial_name,
        "draftsman":draftsman_full_name,
        "detail":drawing_description,
        "path":drawing_file.path,
        "drawing_description":drawing_description

    }

    for picture_id in pictures_id:
        if picture_id.picture_id:
            print('picture id is ')
            print(picture_id.picture_id)
            picture_file = PictureFile.objects.get(pk=picture_id.picture_id.pk)
            print(picture_file.pk)
            try:
                picture_detail = PictureDetail.objects.get(picture_id=picture_file)
                print(picture_detail)
                file_pic_detail = FileDetail.objects.get(pk=picture_detail.detail_id.pk)
                picture_description = file_pic_detail.detail
            except:
                picture_description = "No picture description."
            picture_json = {
                "picture_path":picture_file.path,
                "picture_description":picture_description
            }
            print(picture_json)
            picture_list=np.append(picture_list,picture_json)

    company_position = CompanyPosition.objects.get(position_name="technician")
    profiles_position = ProfilePosition.objects.filter(position_id=company_position.pk)
    for profile_position in profiles_position:
        employee_profile = EmployeeProfile.objects.get(pk=profile_position.profile_id.pk)
        technician_full_name = str(employee_profile.user.pk) + '.' + employee_profile.user.first_name + ' ' + employee_profile.user.last_name
        technicians = np.append(technicians,technician_full_name)
        print(technicians)

    context['drawing_detail'] = selected_drawing
    context['pictures'] = picture_list
    context['technicians'] = technicians
    context['description'] = job_title.description
    return render(request, 'workshop_section/workshop_detail-page.html', context)