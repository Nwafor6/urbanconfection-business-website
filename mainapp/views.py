from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import ProductVideo, Product
from .forms import ProductVideoForm, ContactForm, ProductForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

class IndexView(TemplateView):
    template_name='mainapp/index.html'

class GalleryView(TemplateView):
    template_name='mainapp/gallery.html'

class AboutUs(TemplateView):
    template_name='mainapp/about.html'

class CatalogView(ListView):
    model=Product
    context_object_name='products'
    template_name='mainapp/catalog.html'

class Videos(ListView):
    model=ProductVideo
    context_object_name='videos'
    template_name='mainapp/video.html'

class AdminView(LoginRequiredMixin,ListView):
    model=Product
    template_name='mainapp/admin.html'


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        context['videos']=ProductVideo.objects.all()
        context['p'] = 'hello'
        return context

# class ContactUs(TemplateView):
#     template_name='mainapp/contact-us.html'

def ContactUs(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject='Website Inquiry'
            body ={

            
                "first_name" :form.cleaned_data["first_name"],
                "last_name" : form.cleaned_data["last_name"],
                "email_address":form.cleaned_data["email_address"],
                "message":form.cleaned_data["message"],
            }
            message= "\n".join(body.values())
            try:
                send_mail(subject, message,settings.EMAIL_HOST_USER, ['nwaforglory6@gmail.com'], fail_silently=False)
            except:
                return HttpResponse('Invalid header found.')
        return redirect ('contact-us')
    form = ContactForm
    return render (request, 'mainapp/contact-us.html', {'form': form})


class ProductFormView(LoginRequiredMixin, CreateView):
    form_class=ProductForm
    model=Product
    template_name ='mainapp/admin.html'
    success_url = '/dashboard/'
    success_message = "Product added sucessfully Miss Urban !!!. you've been redirected to your dashboard"



    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['p'] ='message'
        return context

    def post(self,request, *args, **kwargs):
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        




@login_required
def CreateVideo(request):
    page ='video'
    if request.method == 'POST':
        form=ProductVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=ProductVideoForm()
    return render(request,'mainapp/admin.html', {'page':page, 'form':form} )



def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)







