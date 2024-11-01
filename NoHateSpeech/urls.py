"""
URL configuration for NoHateSpeech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# NoHateSpeech/urls.py
from django.urls import path
from .views import home_view, check_value_view  # home_view 추가

urlpatterns = [
    path('', home_view, name='home'),           # 루트 경로에 home_view 연결
    path('check/', check_value_view, name='check_value'),  # /check/ 경로에 check_value_view 연결
]

