from django.contrib import admin
from django.urls import path
from . import views

from .views import (
    demologinIndex,
    demoProfileCreate,
    demoProfileList,
    CreateProfileView,
    SearchProfileView,
)

urlpatterns = [
    path("", demoProfileList, name="profilelist"),
    path("search/<str:para>/", demoProfileList, name="profilesearch"),
    path("raj/<str:para>/", views.raj, name="raj"),
    path("<int:custid>/", demologinIndex, name="profiledetails"),
    path("add/", CreateProfileView.as_view(), name="addpage"),
    path("search/", SearchProfileView.as_view(), name="searchpage"),
]
