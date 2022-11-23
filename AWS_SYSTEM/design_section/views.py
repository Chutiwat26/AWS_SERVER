from django.shortcuts import render, redirect
from django.utils.encoding import *
from django.utils.text import *
from employee_data.models import CompanyPosition, EmployeeProfile, ProfilePosition
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
from customer_section.models import Customers
from django.contrib.auth.models import User
import numpy as np

# Create your views here.

@login_required
def DrawingUpload(request):
    context = {}
    login_user_position_list = []
    login_user = request.user
    #print('login user is '+str(login_user))
    #print(login_user.pk)
    submitter = User.objects.get(username=login_user)
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    #print("Profile id is " + str(login_profile_id))
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        login_user_position_list = np.append(login_user_position_list,login_user_position.position_name)

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False

    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        if login_user_position.position_name == 'draftsman':
            #print(login_user_position.position_name)
            break

    #print("Position id is " + str(login_position_id.pk))
    #print("User position is "+str(login_user_position.position_name))
    if login_user_position.position_name == 'draftsman':
        customer_list = Customers.objects.all()
        context['customer_list'] = customer_list
        if request.method == "POST":
            data = request.POST.copy()
            date_time = datetime.datetime.now()
            datetime_str = str(date_time)
            datetime_convert = datetime_str[0:19] + ':' + datetime_str[20:26]
            #print('datetime is '+datetime_convert)

            #Save job title
            job_title = JobTiltle()
            job_title.title = data.get('drawing_title')
            job_title.description = data.get('drawing_description')
            job_title.submit_date = date_time
            customer = data.get('drawing_customer')
            customer_id = Customers.objects.get(initial_name = customer)
            job_title.customer = customer_id
            job_title.save()

            # Save drawing file
            if 'drawing_file1' in request.FILES:
                drawing = DrawingFile()
                drawing.status = 'waiting'
                file_file1 = request.FILES['drawing_file1']
                #print('file name is ')
                #print(file_file1.name)
                file_file1_name = datetime_convert + '-' + 'drawing1-' + file_file1.name.replace(' ','')
                #print(file_file1_name)
                fs = FileSystemStorage(location='media/file')
                file1_filename = fs.save(file_file1_name, file_file1)
                upload_file1_url = fs.url(file1_filename)
                drawing.path = '/file/' + str(file_file1_name)
                drawing.name = str(file_file1_name)
                drawing.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.drawing_id = DrawingFile.objects.get(name = str(file_file1_name))
                job_file.save()

                file1_detail = data.get('file1_detail')

                if len(file1_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = file1_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_file1_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    drawing_detail = DrawingDetail()
                    drawing_detail.drawing_id = DrawingFile.objects.get(name = str(file_file1_name))
                    drawing_detail.detail_id = FileDetail.objects.get(name = str(file_file1_name))
                    drawing_detail.save()



            if 'drawing_file2' in request.FILES:
                drawing = DrawingFile()
                drawing.status = 'waiting'
                file_file2 = request.FILES['drawing_file2']
                #print('file name is ')
                #print(file_file2.name)
                file_file2_name = datetime_convert + '-' +  'drawing2-' + file_file2.name.replace(' ','')
                #print(file_file2_name)
                fs = FileSystemStorage(location='media/file')
                file2_filename = fs.save(file_file2_name, file_file2)
                upload_file2_url = fs.url(file2_filename)
                drawing.path = '/file/' + str(file_file2_name)
                drawing.name = str(file_file2_name)
                drawing.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.drawing_id = DrawingFile.objects.get(name = str(file_file2_name))
                job_file.save()

                file2_detail = data.get('file2_detail')

                if len(file2_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = file2_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_file2_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    drawing_detail = DrawingDetail()
                    drawing_detail.drawing_id = DrawingFile.objects.get(name = str(file_file2_name))
                    drawing_detail.detail_id = FileDetail.objects.get(name = str(file_file2_name))
                    drawing_detail.save()

            if 'drawing_file3' in request.FILES:
                drawing = DrawingFile()
                drawing.status = 'waiting'
                file_file3 = request.FILES['drawing_file3']
                #print('file name is ')
                #print(file_file3.name)
                file_file3_name = datetime_convert + '-' +  'drawing3-' + file_file3.name.replace(' ','')
                #print(file_file3_name)
                fs = FileSystemStorage(location='media/file')
                file3_filename = fs.save(file_file3_name, file_file3)
                upload_file3_url = fs.url(file3_filename)
                drawing.path = '/file/' + str(file_file3_name)
                drawing.name = str(file_file3_name)
                drawing.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.drawing_id = DrawingFile.objects.get(name = str(file_file3_name))
                job_file.save()

                file3_detail = data.get('file3_detail')

                if len(file3_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = file3_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_file3_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    drawing_detail = DrawingDetail()
                    drawing_detail.drawing_id = DrawingFile.objects.get(name = str(file_file3_name))
                    drawing_detail.detail_id = FileDetail.objects.get(name = str(file_file3_name))
                    drawing_detail.save()

            if 'drawing_file4' in request.FILES:
                drawing = DrawingFile()
                drawing.status = 'waiting'
                file_file4 = request.FILES['drawing_file4']
                #print('file name is ')
                #print(file_file4.name)
                file_file4_name = datetime_convert + '-' +  'drawing4-' + file_file4.name.replace(' ','')
                #print(file_file4_name)
                fs = FileSystemStorage(location='media/file')
                file4_filename = fs.save(file_file4_name, file_file4)
                upload_file4_url = fs.url(file4_filename)
                drawing.path = '/file/' + str(file_file4_name)
                drawing.name = str(file_file4_name)
                drawing.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.drawing_id = DrawingFile.objects.get(name = str(file_file4_name))
                job_file.save()

                file4_detail = data.get('file4_detail')

                if len(file4_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = file4_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_file4_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    drawing_detail = DrawingDetail()
                    drawing_detail.drawing_id = DrawingFile.objects.get(name = str(file_file4_name))
                    drawing_detail.detail_id = FileDetail.objects.get(name = str(file_file4_name))
                    drawing_detail.save()

            if 'drawing_file5' in request.FILES:
                drawing = DrawingFile()
                drawing.status = 'waiting'
                file_file5 = request.FILES['drawing_file5']
                #print('file name is ')
                #print(file_file5.name)
                file_file5_name = datetime_convert + '-' +  'drawing5-' + file_file5.name.replace(' ','')
                #print(file_file5_name)
                fs = FileSystemStorage(location='media/file')
                file5_filename = fs.save(file_file5_name, file_file5)
                upload_file5_url = fs.url(file5_filename)
                drawing.path = '/file/' + str(file_file5_name)
                drawing.name = str(file_file5_name)
                drawing.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.drawing_id = DrawingFile.objects.get(name = str(file_file5_name))
                job_file.save()

                file5_detail = data.get('file5_detail')

                if len(file5_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = file5_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_file5_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    drawing_detail = DrawingDetail()
                    drawing_detail.drawing_id = DrawingFile.objects.get(name = str(file_file5_name))
                    drawing_detail.detail_id = FileDetail.objects.get(name = str(file_file5_name))
                    drawing_detail.save()

            #Save picture file

            if 'drawing_pic1' in request.FILES:
                picture = PictureFile()
                picture.status = ''
                file_pic1 = request.FILES['drawing_pic1']
                file_pic1_name = datetime_convert + '-' +  'picture1-' + file_pic1.name.replace(' ','')
                fs = FileSystemStorage(location='media/picture')
                pic1_filename = fs.save(file_pic1_name, file_pic1)
                upload_pic1_url = fs.url(pic1_filename)
                picture.path = '/picture/' + str(file_pic1_name)
                picture.name = str(file_pic1_name)
                picture.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.picture_id = PictureFile.objects.get(name = str(file_pic1_name))
                job_file.save()

                pic1_detail = data.get('pic1_detail')

                if len(pic1_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = pic1_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_pic1_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    picture_detail = PictureDetail()
                    picture_detail.picture_id = PictureFile.objects.get(name = str(file_pic1_name))
                    picture_detail.detail_id = FileDetail.objects.get(name = str(file_pic1_name))
                    picture_detail.save()

            if 'drawing_pic2' in request.FILES:
                picture = PictureFile()
                picture.status = ''
                file_pic2 = request.FILES['drawing_pic2']
                file_pic2_name = datetime_convert + '-' +  'picture2-' + file_pic2.name.replace(' ','')
                fs = FileSystemStorage(location='media/picture')
                pic2_filename = fs.save(file_pic2_name, file_pic2)
                upload_pic2_url = fs.url(pic2_filename)
                picture.path = '/picture/' + str(file_pic2_name)
                picture.name = str(file_pic2_name)
                picture.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.picture_id = PictureFile.objects.get(name = str(file_pic2_name))
                job_file.save()

                pic2_detail = data.get('pic2_detail')

                if len(pic2_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = pic2_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_pic2_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    picture_detail = PictureDetail()
                    picture_detail.picture_id = PictureFile.objects.get(name = str(file_pic2_name))
                    picture_detail.detail_id = FileDetail.objects.get(name = str(file_pic2_name))
                    picture_detail.save()

            if 'drawing_pic3' in request.FILES:
                picture = PictureFile()
                picture.status = ''
                file_pic3 = request.FILES['drawing_pic3']
                file_pic3_name = datetime_convert + '-' +  'picture3-' + file_pic3.name.replace(' ','')
                fs = FileSystemStorage(location='media/picture')
                pic3_filename = fs.save(file_pic3_name, file_pic3)
                upload_pic3_url = fs.url(pic3_filename)
                picture.path = '/picture/' + str(file_pic3_name)
                picture.name = str(file_pic3_name)
                picture.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.picture_id = PictureFile.objects.get(name = str(file_pic3_name))
                job_file.save()

                pic3_detail = data.get('pic3_detail')

                if len(pic3_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = pic3_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_pic3_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    picture_detail = PictureDetail()
                    picture_detail.picture_id = PictureFile.objects.get(name = str(file_pic3_name))
                    picture_detail.detail_id = FileDetail.objects.get(name = str(file_pic3_name))
                    picture_detail.save()

            if 'drawing_pic4' in request.FILES:
                picture = PictureFile()
                picture.status = ''
                file_pic4 = request.FILES['drawing_pic4']
                file_pic4_name = datetime_convert + '-' +  'picture4-' + file_pic4.name.replace(' ','')
                fs = FileSystemStorage(location='media/picture')
                pic4_filename = fs.save(file_pic4_name, file_pic4)
                upload_pic4_url = fs.url(pic4_filename)
                picture.path = '/picture/' + str(file_pic4_name)
                picture.name = str(file_pic4_name)
                picture.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.picture_id = PictureFile.objects.get(name = str(file_pic4_name))
                job_file.save()

                pic4_detail = data.get('pic4_detail')

                if len(pic4_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = pic4_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_pic4_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    picture_detail = PictureDetail()
                    picture_detail.picture_id = PictureFile.objects.get(name = str(file_pic4_name))
                    picture_detail.detail_id = FileDetail.objects.get(name = str(file_pic4_name))
                    picture_detail.save()

            if 'drawing_pic5' in request.FILES:
                picture = PictureFile()
                picture.status = ''
                file_pic5 = request.FILES['drawing_pic5']
                file_pic5_name = datetime_convert + '-' +  'picture5-' + file_pic5.name.replace(' ','')
                fs = FileSystemStorage(location='media/picture')
                pic5_filename = fs.save(file_pic5_name, file_pic5)
                upload_pic5_url = fs.url(pic5_filename)
                picture.path = '/picture/' + str(file_pic5_name)
                picture.name = str(file_pic5_name)
                picture.save()

                job_file = JobFile()
                job_file.job_id = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
                job_file.picture_id = PictureFile.objects.get(name = str(file_pic5_name))
                job_file.save()

                pic5_detail = data.get('pic5_detail')

                if len(pic5_detail) != 0:
                    file_detail = FileDetail()
                    file_detail.detail = pic5_detail
                    file_detail.submit_datetime = date_time
                    file_detail.name = str(file_pic5_name)
                    file_detail.status = "upload"
                    file_detail.save()

                    picture_detail = PictureDetail()
                    picture_detail.picture_id = PictureFile.objects.get(name = str(file_pic5_name))
                    picture_detail.detail_id = FileDetail.objects.get(name = str(file_pic5_name))
                    picture_detail.save()

            #Save relation of user and job

            user_job = UserJob()
            reponsible_person = User.objects.get(username = login_user.username)
            user_job.user_id = reponsible_person
            #print(data.get('drawing_title'))
            current_job = JobTiltle.objects.get(title = data.get('drawing_title') , submit_date = date_time)
            user_job.job_id = current_job
            user_job.save()

            return redirect('/aws-system-intranet/drawing-upload-done/')
                
        return render(request, 'design_section/drawing_upload-page.html', context)
    else:
        return redirect('/')

@login_required
def DrawingUploadDone(request):
    context = {}
    login_user_position_list = []
    login_user = request.user
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        login_user_position_list = np.append(login_user_position_list,login_user_position.position_name)

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
        
    return render(request, 'design_section/drawing_upload_done-page.html', context)

@login_required
def DrawingStatus(request):
    drawing_wait_list = []
    drawing_process_list = []
    drawing_finish_list = []
    drawing_other_list = []
    drawings_wait = DrawingFile.objects.filter(status = 'waiting')
    drawings_process = DrawingFile.objects.filter(status = 'processing')
    drawings_finish = DrawingFile.objects.filter(status = 'finished')
    drawings_other = DrawingFile.objects.exclude(status = 'waiting').exclude(status = 'processing').exclude(status = 'finished')
    #print('job file are ')
    #print(drawings_wait)
    for drawing_wait in drawings_wait:
        job_files = JobFile.objects.filter(drawing_id = drawing_wait)
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
                    "drawing_name":drawing_wait.name,
                    "drawing_id":drawing_wait.pk,
                    "customer":customer.initial_name,
                    "draftsman":draftsman_id.username,
                    "submit_date":job_title.submit_date,
                    "process_date":job_title.process_date,
                    "finish_date":job_title.finish_date,
                    "status":drawing_wait.status
                }
                drawing_wait_list = np.append(drawing_wait_list,drawing_json)
                #print(drawing_list)
                #print(job_title.title)

    for drawing_process in drawings_process:
        job_files = JobFile.objects.filter(drawing_id = drawing_process)
        drawing_assign = DrawingAssignment.objects.get(drawing_id=drawing_process.pk)
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
                    "drawing_name":drawing_process.name,
                    "drawing_id":drawing_process.pk,
                    "customer":customer.initial_name,
                    "draftsman":draftsman_id.username,
                    "submit_date":job_title.submit_date,
                    "process_date":job_title.process_date,
                    "finish_date":job_title.finish_date,
                    "status":drawing_process.status,
                    "path":drawing_process.path,
                    "responsible_person":drawing_assign.receiver_username
                }
                drawing_process_list = np.append(drawing_process_list,drawing_json)
                #print(drawing_list)
                #print(job_title.title)

    for drawing_finish in drawings_finish:
        job_files = JobFile.objects.filter(drawing_id = drawing_finish)
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
                    "drawing_name":drawing_finish.name,
                    "drawing_id":drawing_finish.pk,
                    "customer":customer.initial_name,
                    "draftsman":draftsman_id.username,
                    "submit_date":job_title.submit_date,
                    "process_date":job_title.process_date,
                    "finish_date":job_title.finish_date,
                    "status":drawing_finish.status,
                    "path":drawing_finish.path
                }
                drawing_finish_list = np.append(drawing_finish_list,drawing_json)
                #print(drawing_list)
                #print(job_title.title)

    for drawing_other in drawings_other:
        job_files = JobFile.objects.filter(drawing_id = drawing_other)
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
                    "drawing_name":drawing_other.name,
                    "drawing_id":drawing_other.pk,
                    "customer":customer.initial_name,
                    "draftsman":draftsman_id.username,
                    "submit_date":job_title.submit_date,
                    "process_date":job_title.process_date,
                    "finish_date":job_title.finish_date,
                    "status":drawing_other.status,
                    "path":drawing_other.path
                }
                drawing_other_list = np.append(drawing_other_list,drawing_json)
                #print(drawing_list)
                #print(job_title.title)

    context = {}
    login_user_position_list = []
    login_user = request.user
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    #login_position_id = ProfilePosition.objects.get(profile_id = login_profile_id)
    #login_user_position = CompanyPosition.objects.get(id=login_position_id.pk)
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        login_user_position_list = np.append(login_user_position_list,login_user_position.position_name)

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
        
    context['drawing_wait_list'] = drawing_wait_list
    context['drawing_process_list'] = drawing_process_list
    context['drawing_finish_list'] = np.flip(drawing_finish_list)
    context['drawing_other_list'] = np.flip(drawing_other_list)
    return render(request, 'design_section/drawing_status-page.html', context)

@login_required
def ShowDrawingDetail(request, drawing_id):
    context = {}
    picture_list=[]
    technicians=[]
    login_user_position_list = []
    date_time = datetime.datetime.now()
    login_user = request.user
    #print('login user is '+str(login_user))
    #print(login_user.pk)
    login_profile_id = EmployeeProfile.objects.get(user=login_user)
    #print("Profile id is " + str(login_profile_id))
    login_position_id = ProfilePosition.objects.filter(profile_id = login_profile_id)
    for position_id in login_position_id:
        login_user_position = CompanyPosition.objects.get(position_name=position_id.position_id.position_name)
        login_user_position_list = np.append(login_user_position_list,login_user_position.position_name)

    if len(login_user_position_list) != 0:
        context['position_list'] = login_user_position_list
        context['position_status'] = True
    else:
        context['position_status'] = False
        
    drawing_file = DrawingFile.objects.get(pk=drawing_id)
    #print(drawing_file)
    job_file = JobFile.objects.get(drawing_id=drawing_file.pk)
    #print(job_file.job_id)
    job_title = JobTiltle.objects.get(pk=job_file.job_id.pk)
    #print(job_title)
    customer = Customers.objects.get(pk=job_title.customer.pk)
    pictures_id = JobFile.objects.filter(job_id=job_file.job_id.pk)
    #print(pictures_id)
    user_job = UserJob.objects.get(job_id=job_title.pk)
    draftsman = User.objects.get(username=user_job.user_id.username)
    draftsman_full_name = draftsman.first_name + ' ' + draftsman.last_name
    sender = login_user.username
    context['position'] = str(login_user_position.position_name)

    if request.method == "POST":
        data = request.POST.copy()
        if str(data.get('drawing_assign')) == '':
            technician_name = data.get('technician_name')
            #print('technician id is ')
            #print(technician_name.split('.')[0])
            #print('technician name is ')
            #print(technician_name.split('.')[1])
            #print('press assign')
            technician_id = int(technician_name.split('.')[0])
            receiver = User.objects.get(pk=technician_id)
            #print(receiver.username)
            #print(sender)
            if len(data.get("drawing_assign_detail")) != 0 :
                file_detail = FileDetail.objects.get(name=drawing_file.name)
                file_detail.detail = data.get("drawing_assign_detail")
                file_detail.status = "processing"
                file_detail.name = drawing_file.name
                file_detail.submit_datetime = date_time
                file_detail.save()

                drawing_assignment = DrawingAssignment()
                drawing_assignment.drawing_id = drawing_file
                drawing_assignment.sender_username = sender
                drawing_assignment.receiver_username = receiver.username
                drawing_assignment.job_state = "processing"
                detail_id = FileDetail.objects.get(submit_datetime=date_time, name=drawing_file.name)
                drawing_assignment.detail_id = detail_id
                drawing_assignment.save()

                #update process date in job title
                job_title.process_date = date_time
                job_title.save()

                #update status in drawing file
                drawing_file.status = "processing"
                drawing_file.save()
            else:
                drawing_assignment = DrawingAssignment()
                drawing_assignment.drawing_id = drawing_file
                drawing_assignment.sender_username = sender
                drawing_assignment.receiver_username = receiver.username
                drawing_assignment.job_state = "processing"
                drawing_assignment.save()

                #update process date in job title
                job_title.process_date = date_time
                job_title.save()

                #update status in drawing file
                drawing_file.status = "processing"
                drawing_file.save()

        elif str(data.get('drawing_cancel')) == '':
            if len(data.get("drawing_cancel_detail")) != 0 :
                file_detail = FileDetail.objects.get(name=drawing_file.name)
                file_detail.detail = data.get("drawing_cancel_detail")
                file_detail.status = "canceled"
                file_detail.name = drawing_file.name
                file_detail.submit_datetime = date_time
                file_detail.save()

                drawing_assignment = DrawingAssignment()
                drawing_assignment.drawing_id = drawing_file
                drawing_assignment.sender_username = sender
                drawing_assignment.receiver_username = ""
                drawing_assignment.job_state = "canceled"
                detail_id = FileDetail.objects.get(submit_datetime=date_time, name=drawing_file.name)
                drawing_assignment.detail_id = detail_id
                drawing_assignment.save()

                #update status in drawing file
                drawing_file.status = "canceled"
                drawing_file.save()
            else:
                drawing_assignment = DrawingAssignment()
                drawing_assignment.drawing_id = drawing_file
                drawing_assignment.sender_username = sender
                drawing_assignment.receiver_username = ""
                drawing_assignment.job_state = "canceled"
                drawing_assignment.save()

                #update status in drawing file
                drawing_file.status = "canceled"
                drawing_file.save()
        return render(request, 'design_section/drawing_action_result-page.html' , context)

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
        "path":drawing_file.path

    }

    for picture_id in pictures_id:
        if picture_id.picture_id:
            #print('picture id is ')
            #print(picture_id.picture_id)
            picture_file = PictureFile.objects.get(pk=picture_id.picture_id.pk)
            #print(picture_file.pk)
            try:
                picture_detail = PictureDetail.objects.get(picture_id=picture_file)
                #print(picture_detail)
                file_pic_detail = FileDetail.objects.get(pk=picture_detail.detail_id.pk)
                picture_description = file_pic_detail.detail
            except:
                picture_description = "No picture description."
            picture_json = {
                "picture_path":picture_file.path,
                "picture_description":picture_description
            }
            #print(picture_json)
            picture_list=np.append(picture_list,picture_json)

    company_position = CompanyPosition.objects.get(position_name="technician")
    profiles_position = ProfilePosition.objects.filter(position_id=company_position.pk)
    for profile_position in profiles_position:
        employee_profile = EmployeeProfile.objects.get(pk=profile_position.profile_id.pk)
        technician_full_name = str(employee_profile.user.pk) + '.' + employee_profile.user.first_name + ' ' + employee_profile.user.last_name
        technicians = np.append(technicians,technician_full_name)
        #print(technicians)

    context['drawing_detail'] = selected_drawing
    context['pictures'] = picture_list
    context['technicians'] = technicians
    context['description'] = job_title.description
    return render(request, 'design_section/drawing_detail-page.html', context)

