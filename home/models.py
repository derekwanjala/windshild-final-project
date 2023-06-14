from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    detail = RichTextUploadingField(blank=True)
    short_detail = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])

    def __str__(self):
        return self.title


class About(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    detail = RichTextUploadingField(blank=True)
    short_detail = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.title


class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
