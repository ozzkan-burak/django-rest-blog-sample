#Listelme işlemleri için kullanılan class
from rest_framework.generics import ListAPIViews

from post.models import Post

class PostListAPIView(ListAPIViews):
  queryset = Post.objects.all()
  
