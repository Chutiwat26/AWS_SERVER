from django.shortcuts import render
from employee_data.models import *
import numpy as np

# Create your views here.
def Home(request):
    context = {}
    login_user_position_list=[]
    try:
        login_username = request.user.username
        user_detail = User.objects.get(username=login_username)
        login_user_pk = str(user_detail.pk) + "." + user_detail.username
        employee_profile = EmployeeProfile.objects.get(user = user_detail.pk)
        position_list = ProfilePosition.objects.filter(profile_id = employee_profile.pk)

        for user_position in position_list:
            position_name = CompanyPosition.objects.get(pk=user_position.position_id.pk)
            login_user_position_list = np.append(login_user_position_list,position_name.position_name)

        if len(login_user_position_list) != 0:
            context['position_list'] = login_user_position_list
            context['position_status'] = True
        else:
            context['position_status'] = False
            
    except:
        #print("no login")
        pass
        
    context['homepage_message_1'] = 'บริษัท แอ็ดว๊านซ์ แอนด์ ไวส์ โซลูชั่น จำกัด'
    context['homepage_message_2'] = 'บริษัท แอ็ดว๊านซ์ แอนด์ ไวส์ โซลูชั่น เป็นบริษัทที่จัดตั้งขึ้นมาเพื่อผลิตชิ้นส่วนเครื่องจักร เครื่องจักรและระบบอัตโนมัติ ที่มีคุณภาพสูงแก่ลูกค้า นอกจากการผลิตแล้วเรายังยินดีให้บริการการออกแบบเครื่องจักร การทำแบบ 2 มิติ การทำระบบไฟฟ้า และการทำโปรแกรมตามความต้องการให้เสร็จสมบูรณ์ภายในระยะเวลาที่กำหนด พร้อมกับบริการหลังการขายที่ดีเยี่ยม'
    context['homepage_message_3'] = 'เรามีประสบการณ์ทำงานให้กับหลากหลายภาคอุตสาหกรรม ไม่ว่าจะเป็นอุตสาหกรรมอาหาร อุตสาหกรรมยา อุตสาหกรรม ยานยนต์และอุตสาหกรรมอิเล็คทรอนิกส์ เรายินดีเป็นอย่างยิ่งที่จะนำความรู้ ความสามารถของเราไปสรรค์สร้าง พัฒนาและให้ บริการเพื่อตอบสนองความต้องการของลูกค้าทุกท่าน'
    return render(request, 'aws_homepage/homepage-index.html', context)

def About(request):
    return render(request, 'aws_homepage/homepage-about.html')