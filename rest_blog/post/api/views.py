#Listelme işlemleri için kullanılan class
from rest_framework.generics import ListAPIView

from post.models import Post

class PostListAPIView(ListAPIView):
  queryset = Post.objects.all()
  
