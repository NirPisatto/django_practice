"""
URL configuration for storage_service project.

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
from django.urls import path
from storage_api.views import FileList, FileCreate, File
# from storage_api.views import get_all_files, handle_file, FileUploadAPIView

# urlpatterns = [
#     path('', get_all_files),
#     path('<int:file_id>', handle_file),
#     path('file', FileUploadAPIView.as_view(), name='file-upload'),
# ]

urlpatterns = [
    path('', FileList.as_view()),
    path('upload', FileCreate.as_view()),
    path('<int:file_id>', File.as_view()),
]