"""
URL configuration for petpal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to PetPal!")


urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),
    path('api/', include('pet.urls')),  # Include the pet app URLs
    path('api/store/', include('store.urls')),
    path('api/lostfound/', include('lostfound.urls')),
    path('api/pet/', include('pet.urls')),
    path('api/user/', include('user.urls')),
    path('api/rehabiliation/', include('rehabiliation.urls')),
    path('', include('store.urls')),  # Include the store app's URLs
     path('', include('rehabiliation.urls')),
     path('', include('lostfound.urls')),
]


