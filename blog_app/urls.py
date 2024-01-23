from django.urls import path, re_path
from . import views

app_name = "blog_app"

urlpatterns = [
    path("createblog/", views.BlogCreateLogic.as_view(), name="createblog"),
    path("<slug:slug>", views.BlogReadUpdateDeleteLogic.as_view(), name=""),
]
