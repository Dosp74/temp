from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    main_image = models.ImageField(upload_to='product/images/%Y/%m/%d/', blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)