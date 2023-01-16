
from django.urls import path
from . import views
urlpatterns = [
    path("helloworld/", views.helloworld),
    path("",views.taskList, name = "taskList"),
    path("sobre", views.sobre, name = "sobre"),
    path("about",views.about, name="about")
]
