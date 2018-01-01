"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from django.views import static
from home.views import get_index
from threads import views as forum_views
from django.views.generic import TemplateView
from contact.views import contact

from products import urls as urls_products
from products.views import product_list
from products import urls as product_urls




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    
    #Forum
    url(r'^forum/$', forum_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

    
    url(r'^about', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^location', TemplateView.as_view(template_name='location.html'),name='location'),
    url(r'^class_timetable', TemplateView.as_view(template_name='class_timetable.html'),name='class_timetable'),
    url(r'^class_descriptions', TemplateView.as_view(template_name='class_descriptions.html'),name='descriptions'),
    url(r'^contact/', contact, name='contact'),
    
    #Courses
    url(r'^courses/', product_list, name='courses'),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
]
