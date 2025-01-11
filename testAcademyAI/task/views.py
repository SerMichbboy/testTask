from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(APIView):
    """
        Операции с моделью Task:
            - Получение списка задач (GET /tasks/).
            - Создание новой задачи (POST /tasks/).
    """
    def get(self, request):
        """
            Получение списка задач.
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            serializer.data
        )

    def post(self, request):
        """
            Создание новой задачи.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
