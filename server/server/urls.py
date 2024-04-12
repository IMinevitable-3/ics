from django.contrib import admin
from django.urls import path
from rest_api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/get-grid", views.GetDistanceAndLoc().as_view()),
]
