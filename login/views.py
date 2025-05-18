from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(f"Authenticated User: {user}")

        if user is not None:
            login(request, user)
            return redirect('task_view')
        else:
            messages.error(request, 'Invalid username or password.')

    # Ensure the template is rendered for both GET and unsuccessful POST requests
    return render(request, 'login.html')


class CTMLogoutView(LogoutView):
    next_page = reverse_lazy('login')


@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User added successfully.')
            return redirect('list_users')

    return render(request, 'add_user.html')


@login_required
def list_users(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'list_users.html', {'users': users})


@login_required
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, 'User deleted successfully.')
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
    return redirect('list_users')


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, 'Email is already registered.')
        else:
            user.username = username
            user.email = email
            user.save()
            messages.success(request, 'User updated successfully.')
            return redirect('list_users')

    return render(request, 'edit_user.html', {'user': user})
