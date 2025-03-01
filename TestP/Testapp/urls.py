from django.urls import path
from .views import process_voice,api,user_login,dashboard,show_experiments,completed,pending,ytb,titration

urlpatterns = [
    path("process_voice/", process_voice, name="process_speech"),
    path("api",api,name="api"),
    path("login/",user_login,name="login"),
    path("dashboard/",dashboard,name="dashboard"),
    path("experiments/", show_experiments, name="show_experiments"),
    path("completed/",completed,name="completed"),
    path("pending/",pending,name="pending"),
    path("ytb/",ytb,name="ytb"),
    path("titration/",titration,name="titration")
    ]
