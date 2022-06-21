from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):

    CATEGORY=[
        ('wedding Cake', 'Wedding Cake'),
         ('Birthday Cake', 'Birthday Cake'),
         ('Snacks', 'Snacks')
    ]

    title=models.CharField(max_length=200)
    slug=models.SlugField()
    price=models.PositiveIntegerField(default=0)
    img=models.FileField()
    category=models.CharField(max_length=100, choices=CATEGORY)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Product, self).save(*args, **kwargs)

class ProductVideo(models.Model):
    video_title=models.CharField(max_length=100)
    slug=models.SlugField()
    video=models.FileField()
    date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-date',)

    def __str__(self):
        return f"{self.video_title} | {self.date}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.video_title)
        super(ProductVideo, self).save(*args, **kwargs)

    