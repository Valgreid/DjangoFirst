"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MainApp import views

urlpatterns = [
    path('', views.home),  # http://127.0.0.1:8000
    path('item/<int:id>', views.item_page), # http://127.0.0.1:8000/item/1 http://127.0.0.1:8000/item/2
    path('items', views.items_list), # http://127.0.0.1:8000/item/1 http://127.0.0.1:8000/item/2
    path('page-1', views.page1), # http://127.0.0.1:8000/item/1 http://127.0.0.1:8000/item/2
]

# 1. Функции-обработчики
# 2. CBV
#ooo