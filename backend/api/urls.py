"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    # API entry points should be defined here
    path('test.json', views.test_api_view, name='api test'),
    path('exercise-api-view', views.exercise_api_view, name='exercise api view'),
    path('workout-api-view', views.workout_api_view, name= 'workout api view'),
    path('workout-exercise-view', views.workout_exercise_api_view, name='workout exercise api view')
]