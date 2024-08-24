from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name="comments")
    discrition = models.TextField()
    author = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)