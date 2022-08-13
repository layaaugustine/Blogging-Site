from distutils.command.upload import upload
from email.policy import default
from re import fullmatch
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts",default="")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)]) 
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='posts')
    tag = models.ManyToManyField(Tag,)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments",default=" ")