
from django.urls import path, include

from .views import demo, redirectdemo,MyDemoView

"""
http://xyz.com/profiles/

"""

urlpatterns = [
    path("demo/demo/", demo, name = "profilelanding"),
    path("redirectdemo/", redirectdemo, name = "redirectdemo"),
    path("viewdemo/", MyDemoView.as_view(), name = "viewdemo")
]
