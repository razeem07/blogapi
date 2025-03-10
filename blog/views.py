from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView

from  rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions

from blog.serializers import UserCreationSerializers,PostSerializers,CommentSerializer

from blog.models import Post

# Create your views here.



class UserCreateView(CreateAPIView):

    serializer_class=UserCreationSerializers


class PostListCreateView(ListAPIView,CreateAPIView):
      
      authentication_classes=[authentication.TokenAuthentication]

      permission_classes=[permissions.IsAuthenticated]

      serializer_class=PostSerializers

      queryset=Post.objects.all()

      def perform_create(self,serializer):
           
           return serializer.save(owner=self.request.user)


class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
     
     authentication_classes=[authentication.TokenAuthentication]

     permission_classes=[permissions.IsAuthenticated]

     serializer_class=PostSerializers

     queryset=Post.objects.all()
     
     
class CommentCreateView(CreateAPIView):
     
     serializer_class=CommentSerializer

     authentication_classes=[authentication.TokenAuthentication]

     permission_classes=[permissions.IsAuthenticated]


     def perform_create(self,serializer):
          
          id=self.kwargs.get("pk")

          post_instance=get_object_or_404(Post,id=id)

          serializer.save(post_object=post_instance,owner=self.request.user)


class PostLikeView(APIView):

     authentication_classes=[authentication.TokenAuthentication]

     permission_classes=[permissions.IsAuthenticated]

     def post(self,request,*args,**kwargs):

          id=kwargs.get("pk")

          post_object = get_object_or_404(Post,id=id)

          if request.user in post_object.liked_by.all():

              post_object.liked_by.remove(request.user)
 
              return Response(data={"message":"liked"})
          
          else:

              post_object.liked_by.add(request.user)
 
              return Response(data={"message":"liked"})
