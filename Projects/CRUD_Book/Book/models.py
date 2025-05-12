from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=255)
    book_publisher = models.CharField(max_length=255)
    book_price = models.IntegerField()