"""collaborative_task_manager URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function task_views
    1. Add an import:  from my_app import task_views
    2. Add a URL to urlpatterns:  url(r'^$', home, name='home')
Class-based task_views
    1. Add an import:  from other_app.task_views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import *

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet, basename='task')
# router.register(r'updates', TaskUpdateViewSet, basename='update')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('', include('login.urls')),
    path('task/', task_view, name='task_view'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:task_id>/add_user/', add_users_task, name='add_users_task'),
    path('task/<int:task_id>/', task_data_view, name='task_data_view'),
    path('task/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('task/<int:task_id>/task_update/', get_user_task_update, name='get_user_task_update'),
    path('task/<int:task_id>/user_view/', user_task_view, name='user_task_view'),
]

