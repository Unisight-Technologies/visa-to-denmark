from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from . import mailhandler
from . import models
#recaptcha imports
import json
import urllib
from django.conf import settings
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()


class Homepage(TemplateView):
    template_name= "index.html"

class Contact(View):
    def get(self, request, *args, **kwargs):
        context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
        }

        return render(request, "contact.html",context = context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        if result['success']:
            mailhandler.sendMailToUser(request.POST.get('name'), request.POST.get('email'))
            mailhandler.sendMailToVisaToDenmark(request.POST.get('name'), request.POST.get('email'),request.POST.get('phone'),request.POST.get('subject'),request.POST.get('message'))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.info(request, 'Invalid reCAPTCHA. Please try again.')
            context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
            }
            return render(request, "contact.html",context = context)
        

class about(TemplateView):
    template_name= "aboutus.html"

class student(TemplateView):
    template_name= "student.html"

class workvisa(TemplateView):
        template_name= "workvisa.html"

class denmarkstartupvisa(TemplateView):
        template_name= "denmarkstartupvisa.html"
class family(TemplateView):
        template_name= "family.html"

class policy(TemplateView):
    template_name= "policy.html"

class terms(TemplateView):
    template_name= "terms.html"

class general(TemplateView):
    template_name= "generaldisclaimer.html"

class givesit(TemplateView):
    template_name= "givesit.html"

class News(View):
    def get(self, request, *args, **kwargs):
        news=models.News.objects.all()
        context={
        "all_news":news,
        "info":"mydata",


        }
        print(news)

        return render(request, "news.html",context=context)
