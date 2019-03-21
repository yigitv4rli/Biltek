from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.CharField(max_length=20)
    body = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    image = models.ImageField()
    mainornot = models.CharField(max_length=50,default='Hayır')
    #add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:200] +"..."

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE, verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name = "isim")
    comment_content = models.CharField(max_length=300,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
