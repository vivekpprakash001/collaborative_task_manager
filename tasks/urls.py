from django.urls import path
# from .views import task_view
# from .views import TaskCreateView
# from .views import add_users_task
# from .views import task_data_view
# from .views import edit_task
# from .views import delete_task
# from .views import user_task_view
# from .views import get_user_task_update
#
# urlpatterns = [
#     path('task_view/', task_view, name='task_view'),
#     path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
#     path('tasks/<int:task_id>/add_user/', add_users_task, name='add_users_task'),
#     path('tasks/<int:task_id>/', task_data_view, name='task_data_view'),
#     path('tasks/<int:task_id>/edit/', edit_task, name='edit_task'),
#     path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
#     path('tasks/<int:task_id>/user_view', user_task_view, name='user_task_view'),
#     path('tasks/task_udpate/<int:task_id>', get_user_task_update, name='get_user_task_update')
# ]

# from . import views  # Import from the tasks_app views
#
# urlpatterns = [
#     path('', views.task_view, name='task_view'),
#     path('create/', views.TaskCreateView.as_view(), name='task_create'),
#     path('<int:task_id>/add_user/', views.add_users_task, name='add_users_task'),
#     path('<int:task_id>/', views.task_data_view, name='task_data_view'),
#     path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
#     path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
#     path('<int:task_id>/user_view/', views.user_task_view, name='user_task_view'),
#     path('<int:task_id>/task_update/', views.get_user_task_update, name='get_user_task_update'),
# ]
