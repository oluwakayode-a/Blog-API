from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, max_length=500)
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    