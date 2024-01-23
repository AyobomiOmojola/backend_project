from django.shortcuts import render
from rest_framework.decorators import APIView 
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import BlogSerializer
from .models import Blog


# Create your views here.

### Create your blog
class BlogCreateLogic(APIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)

            response = {
                "MESSAGE":"Blog Created!!!",
                "BLOG":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogReadUpdateDeleteLogic(APIView):
        permission_classes = [permissions.IsAuthenticated]

        ### Read/Retrieve a blog
        def get(self, request:Request, slug):
            blog = Blog.objects.get(slug=slug)
            blog_serializer = BlogSerializer(instance=blog)

            response = {
                "MESSAGE": "This is the blog you requested for",
                "BLOG": blog_serializer.data
            }

            return Response(data = response, status = status.HTTP_200_OK )

        ### Update your blog
        def put(self, request:Request, slug):
            blog = Blog.objects.get(slug=slug)
            if request.user == blog.author:
                data = request.data
                serializer = BlogSerializer(instance = blog, data = data)

                if serializer.is_valid():
                    serializer.save()

                    response={
                        "MESSAGE": "Blog Updated Successfully!!!",
                        "BLOG":serializer.data
                    }


                    return Response(data=response, status=status.HTTP_200_OK)

                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'Message': 'You are not the author of this blog!'},status=status.HTTP_400_BAD_REQUEST)
        
        ### Delete your blog
        def delete(self, request:Request, slug):
            blog = Blog.objects.get(slug=slug)
            if request.user == blog.author:
                blog.delete()

                return Response({"MESSAGE": "You just deleted this blog"},status=status.HTTP_200_OK)
            return Response({'Message': 'You are not the author of this blog!'},status=status.HTTP_400_BAD_REQUEST)
