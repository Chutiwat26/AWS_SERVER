"""AWS_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('aws-system/admin/', admin.site.urls),
    path('aws-system-intranet/', include('employee_data.urls')),
    path('aws-system-intranet/', include('design_section.urls')),
    path('aws-system-intranet/', include('workshop_section.urls')),
    path('aws-system-intranet/', include('admin_section.urls')),
    path('aws-system-intranet/', include('purchase_section.urls')),
    path('aws-customer/', include('customer_section.urls')),
    path('', include('aws_homepage.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)