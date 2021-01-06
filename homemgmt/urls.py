"""homemgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
            url('admin/', admin.site.urls),
            url('trigger_main_gate', views.trigger_main_gate, name='trigger_main_gate'),
            url('trigger_garage_gate', views.trigger_garage_gate, name='trigger_garage_gate'),
            url('turn_on_terrace_lights', views.turn_on_terrace_lights, name='turn_on_terrace_lights'),
            url('turn_off_terrace_lights', views.turn_off_terrace_lights, name='turn_off_terrace_lights'),
            url('', views.home, name='home'),
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
