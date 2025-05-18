from django.urls import path
from .views import login_view
from .views import home
from .views import CTMLogoutView
from .views import add_user
from .views import list_users
from .views import delete_user
from .views import edit_user

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', CTMLogoutView.as_view(), name='logout'),
    path('add_user/', add_user, name='add_user'),
    path('list_users/', list_users, name='list_users'),
    path('edit_user/<int:user_id>', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user'),
]
