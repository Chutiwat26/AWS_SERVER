from django.shortcuts import render
from employee_data.models import *

# Create your views here.
def Home(request):
    context = {}
    try:
        login_user = request.user
        print('login user is '+str(login_user))
        print(login_user.pk)
        login_profile_id = EmployeeProfile.objects.get(user=login_user)
        print("Profile id is " + str(login_profile_id))
        login_position_id = ProfilePosition.objects.get(profile_id = login_profile_id)
        print("Position id is " + str(login_position_id.pk))
        login_user_position = CompanyPosition.objects.get(id=login_position_id.pk)
        print("User position is "+str(login_user_position.position_name))
        context['position'] = str(login_user_position.position_name)
    except:
        print("no login")
        
    context['homepage_message_1'] = 'บริษัท แอ็ดว๊านซ์ แอนด์ ไวส์ โซลูชั่น จำกัด'
    context['homepage_message_2'] = 'บริษัท แอ็ดว๊านซ์ แอนด์ ไวส์ โซลูชั่น เป็นบริษัทที่จัดตั้งขึ้นมาเพื่อผลิตชิ้นส่วนเครื่องจักร เครื่องจักรและระบบอัตโนมัติ ที่มีคุณภาพสูงแก่ลูกค้า นอกจากการผลิตแล้วเรายังยินดีให้บริการการออกแบบเครื่องจักร การทำแบบ 2 มิติ การทำระบบไฟฟ้า และการทำโปรแกรมตามความต้องการให้เสร็จสมบูรณ์ภายในระยะเวลาที่กำหนด พร้อมกับบริการหลังการขายที่ดีเยี่ยม'
    context['homepage_message_3'] = 'เรามีประสบการณ์ทำงานให้กับหลากหลายภาคอุตสาหกรรม ไม่ว่าจะเป็นอุตสาหกรรมอาหาร อุตสาหกรรมยา อุตสาหกรรม ยานยนต์และอุตสาหกรรมอิเล็คทรอนิกส์ เรายินดีเป็นอย่างยิ่งที่จะนำความรู้ ความสามารถของเราไปสรรค์สร้าง พัฒนาและให้ บริการเพื่อตอบสนองความต้องการของลูกค้าทุกท่าน'
    return render(request, 'aws_homepage/homepage-index.html', context)

def About(request):
    return render(request, 'aws_homepage/homepage-about.html')