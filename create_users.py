import os
import django

# Set up Django environment (adjust 'your_project_name' to your actual project folder)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collaborative_task_manager.settings')
django.setup()

from django.contrib.auth.models import User

users_info = [['admin', 'admin@ctm.com', 'q1w2e3r4', 1], ['user1', 'user1@ctm.com', 'u1@q1w2e3r4', 0], ['user2', 'user2@ctm.com', 'u2@q1w2e3r4', 0]]

for i in users_info:
    if i[3] == 1:
        user = User.objects.create_superuser(username=i[0], email=i[1], password=i[2])
        print(f'User "{i[0]}" created successfully!')
    else:
        if not User.objects.filter(username=i[0]).exists():
            user = User.objects.create_user(username=i[0], email=i[1], password=i[2])
            print(f'User "{i[0]}" created successfully!')
        else:
            print(f'User "{i[0]}" already exists.')
