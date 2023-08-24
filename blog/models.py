from django.db import models
from account.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Delete")
)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    f_image = models.ImageField(upload_to='blog-image/')
    image = models.ImageField(upload_to='content-image/')
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modeified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modeified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.user} comment on {self.post.title}'