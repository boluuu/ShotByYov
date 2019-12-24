from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    image = models.ImageField(upload_to="post_image", blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='portfolios')
    description = models.TextField()

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.email