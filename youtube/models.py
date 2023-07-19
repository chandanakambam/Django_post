from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=225,null=True,blank=True)
    image_url = models.URLField(blank=True)
    def __str__(self):
        return self.title
