"""visa_to_denmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from visa_to_denmark_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage.as_view(),name="index"),
    path('contact/',views.Contact.as_view(),name="contact"),
    path('about/',views.about.as_view(),name="about"),
    path('student/',views.student.as_view(),name="student"),
    path('workvisa/',views.workvisa.as_view(),name="workvisa"),
    path('visitorvisa/',views.visitorvisa.as_view(),name="visitorvisa"),
    path('family/',views.family.as_view(),name="family"),path('policy/',views.policy.as_view(),name="policy"),
    path('terms/',views.terms.as_view(),name="terms"),
    path('generaldisclaimer/',views.general.as_view(),name="general"),
    path('givesit/',views.givesit.as_view(),name="givesit"),
    path('news/',views.News.as_view(),name="news"),
]
