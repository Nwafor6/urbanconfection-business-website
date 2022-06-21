from django.urls import path
from.import views
from .views import (IndexView, GalleryView, 
    AboutUs, CatalogView,CreateVideo, 
    AdminView,Videos, ProductFormView)

urlpatterns=[

    path('', IndexView.as_view(), name='home-page'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('dashboard/', AdminView.as_view(), name='dashboard'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('our-catalog/', CatalogView.as_view(), name='our-catalog'),
    # path('contact-us/', ContactUs.as_view(), name='contact-us'),
    path('contact-us/', views.ContactUs, name='contact-us'),
    # path('post-video/', CreateVideo.as_view(), name='post-video'),
    path('videos/', Videos.as_view(), name='videos'),
    path('dashboard/post-video/', views.CreateVideo, name='post-video'),
    path('dashboard/post-product/', ProductFormView.as_view(), name='post-product'),

]