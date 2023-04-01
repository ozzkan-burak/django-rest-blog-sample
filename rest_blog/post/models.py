from django.db import models

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=120)
  content = models.TextField()