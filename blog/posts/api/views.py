from django.http import response
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializer import PostSerializer


# class PostApiView(APIView):
#     def get(self, request):
#         # posts = Post.objects.all()
#         # posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many = True)
#         return Response(status = status.HTTP_200_OK, data = serializer.data)

#     def post(self, request):
#         # Post.objects.create(title = request.POST['title'],
#         #                     description = request.POST['description'],
#         #                     order = request.POST['order'])
#         # return self.get(request)
#         serializer = PostSerializer(data = request.POST)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(status = status.HTTP_200_OK, data = serializer.data)

# class PostViewSet(ViewSet):
#     def list(self, request):
#         # posts = Post.objects.all()
#         # posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def retrieve(self, request, pk: int):
#         post = PostSerializer(Post.objects.get(pk = pk))
#         return Response(status = status.HTTP_200_OK, data = post.data)

#     def create(self, request):
#         # Post.objects.create(title = request.POST['title'],
#         #                     description = request.POST['description'],
#         #                     order = request.POST['order'])
#         # return self.get(request)
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# OBTENIENDO EL CRUD COMPLETO CON 2 LÍNEAS DE CÓDIGO
class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # Se pueden limitar las tipos de peticiones
    # http_method_names = ['get', 'post']

