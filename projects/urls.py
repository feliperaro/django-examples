from django.urls import path
from projects.views import (ProjectCreateAPIView, ProjectDestroyAPIView, ProjectListAPIView, ProjectUpdateAPIView)

app_name = 'projects'

urlpatterns = [
    path('api/create/', ProjectCreateAPIView.as_view(), name='project_create_api_view'),
    path('api/update/<uuid:pk>/', ProjectUpdateAPIView.as_view(), name='project_update_api_view'),
    path('api/delete/<uuid:pk>/', ProjectDestroyAPIView.as_view(), name='project_delete_api_view'),
    path('api/list/', ProjectListAPIView.as_view(), name='project_list_api_view')
]