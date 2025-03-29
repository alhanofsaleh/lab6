from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)  # عنوان الكتاب
    author = models.CharField(max_length=50)  # المؤلف
    price = models.FloatField(default=0.0)  # سعر الكتاب
    edition = models.SmallIntegerField(default=1)  # رقم الإصدار
