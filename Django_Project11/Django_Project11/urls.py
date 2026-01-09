from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # List + Create
    path('studentapi/', views.StudentAPI.as_view()),

    # Update (needs pk)
    path('studentapi/<int:pk>/', views.StudentAPI.as_view()),
]
