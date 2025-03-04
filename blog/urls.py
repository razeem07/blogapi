from django.urls import path

from blog import views



urlpatterns=[

    path("users/",views.UserCreateView.as_view()),

    path("posts/",views.PostListCreateView.as_view()),

    path("posts/<int:pk>/",views.PostRetrieveUpdateDestroyView.as_view()),

    path("posts/<int:pk>/comments/",views.CommentCreateView.as_view()),


    
    
]