from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Task
from .models import TaskUsers
from .models import TaskUpdate

from .forms import TaskForm

from .utils import queryset_to_dict_list


@login_required
def task_view(request):
    user = request.user
    if user.is_superuser:
        tasks = Task.objects.all()
    else:
        task_users = TaskUsers.objects.filter(user=user)
        tasks_list = [i.task_id for i in task_users]
        tasks = Task.objects.filter(id__in=tasks_list)
    context = {'task_data': queryset_to_dict_list(tasks)}
    return render(request, 'tasks_list.html', context=context)


class TaskCreateView(LoginRequiredMixin, View):
    template_name = 'tasks.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('add_users_task', task_id=task.id)
        return render(request, self.template_name, {'form': form})


@login_required
def add_users_task(request, task_id):
    users = User.objects.filter(is_superuser=False).values('id', 'username')
    limit = len(users)
    errors = {}
    success_message = ''

    if request.method == 'POST':
        fields = request.POST.getlist('fields[]')
        try:
            task = get_object_or_404(Task, id=task_id)
            for user_id in fields:
                user = get_object_or_404(User, id=user_id)
                TaskUsers.objects.create(task=task, user=user)
            success_message = 'Tasks and Users are assigned successfully'
        except Exception as e:
            errors['exception'] = str(e)
            print(errors)

    return render(request, 'task_add_users.html', {
        'users': list(users),
        'limit': limit,
        'errors': errors,
        'success_message': success_message
    })


@login_required
def task_data_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task_users = TaskUsers.objects.filter(task=task)
    data = {
        'task_title': task.title,
        'description': task.description,
        'created_at': task.created_at,
        'updated_at': task.updated_at,
        'status': task.status,
        'users': []
    }
    for user in task_users:
        user_data = User.objects.get(id=user.user_id)
        data['users'].append({
            'user_id': user.user_id,
            'user_name': user_data.username
        })

    print(data)
    return render(request, 'task_view.html', context=data)


@login_required()
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('add_users_task', task_id=task.id)  # Redirect after saving
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks.html', {'form': form, 'task': task})


@login_required()
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_view')
    return redirect('task_view')


@login_required()
def user_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task_update = TaskUpdate.objects.filter(task_id=task_id)
    if len(task_update) > 0:
        updated_at = task_update.latest('timestamp').timestamp
    else:
        updated_at = task.updated_at
    update_data = []
    for i in task_update:
        update_data.append({
            'update_text': i.update_text,
            'task_id': i.task_id,
            'timestamp' : i.timestamp,
            'user_name': i.updated_by.username
        })
    data = {
        'task_id': task_id,
        'task_title': task.title,
        'description': task.description,
        'created_at': task.created_at,
        'updated_at': updated_at,
        'status': task.status,
        'updates': update_data
    }
    print(data)
    return render(request, 'tasks_view_users.html', context=data)


@csrf_exempt
def get_user_task_update(request, task_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

    update_text = request.POST.get('update_text')
    print('*' * 10)
    print(task_id)
    print('*' * 10)
    print(update_text)
    print('*' * 10)
    user_name = request.POST.get('user_name')
    print(user_name)
    print('*' * 10)

    if not update_text or not user_name:
        return JsonResponse({'error': 'Missing update_text or user_id'}, status=400)

    try:
        # Fetch user instance; updated_by expects a User instance, not an ID
        updated_by_user = User.objects.get(username=user_name)
        # Make sure task exists (optional but recommended)
        task = Task.objects.get(id=task_id)

        task_update = TaskUpdate.objects.create(
            task=task,
            updated_by=updated_by_user,
            update_text=update_text
        )
        return JsonResponse({
            'success': True,
            'task_update_id': task_update.id,
            'timestamp': task_update.timestamp.isoformat(),
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
