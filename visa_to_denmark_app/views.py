from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from . import mailhandler










class Homepage(TemplateView):
    template_name= "index.html"

class Contact(View):
    def get(self, request, *args, **kwargs):
        print("GET")

        return render(request, "contact.html")

    def post(self, request, *args, **kwargs):
        data = request.POST
        mailhandler.sendMailToUser(data.get('name'), data.get('email'))
        mailhandler.sendMailToVisaToDenmark(data.get('name'), data.get('email'),data.get('phone'),data.get('subject'),data.get('message'))

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')

class about(TemplateView):
    template_name= "aboutus.html"

class student(TemplateView):
    template_name= "student.html"

class workvisa(TemplateView):
        template_name= "workvisa.html"

class visitorvisa(TemplateView):
        template_name= "visitorvisa.html"
class family(TemplateView):
        template_name= "family.html"
