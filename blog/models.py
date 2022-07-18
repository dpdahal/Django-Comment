from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title


# comments models here
class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_comments(self):
        return Comment.objects.filter(parent=self)
