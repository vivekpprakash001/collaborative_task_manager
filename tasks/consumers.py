import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Task, TaskUpdate
from .serializers import TaskSerializer, TaskUpdateSerializer
from django.contrib.auth.models import User

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'tasks'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')
        task_data = data.get('task')

        if action == 'update':
            await self.create_task_update(task_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'task_update',
                'message': task_data
            }
        )

    async def task_update(self, event):
        await self.send(text_data=json.dumps(event['message']))

    @sync_to_async
    def create_task_update(self, task_data):
        task_id = task_data.get('id')
        update_text = task_data.get('update_text')
        user_id = task_data.get('user_id')
        try:
            task = Task.objects.get(id=task_id)
            user = User.objects.get(id=user_id)
            TaskUpdate.objects.create(task=task, updated_by=user, update_text=update_text)
        except Task.DoesNotExist:
            pass
        except User.DoesNotExist:
            pass
