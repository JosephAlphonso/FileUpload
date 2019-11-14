from django.urls import path

from . import views

app_name = "file_upload_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('view_data/', views.view_data, name='view_data'),
    path('search/', views.search_function, name='search_function'),
    
]