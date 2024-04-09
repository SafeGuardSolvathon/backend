from .models import Chat
from .serializer import ChatSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def chat(request, format=None):
    if request.method == 'GET':
        post = Chat.objects.all()
        serializer = ChatSerializer(post, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            post_data = serializer.data
            response_data={
                'success': True,
                'details': post_data
            }
            return JsonResponse(response_data, status = 201)
        else:
            return JsonResponse({'error':'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error':'Invalid request method'}, status = 400)

@api_view(['GET','PUT','DELETE','POST'])
def chat_detail(request, id, format=None):

    try:
        chats = Chat.objects.get(pk=id)
    except Chat.DoesNotExist:
        #To check is something is a valid request
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #Takes object in get
        serializer = ChatSerializer(chats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChatSerializer(chats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        chats.save()
        serializer = ChatSerializer(chats)
        return Response(serializer.data)