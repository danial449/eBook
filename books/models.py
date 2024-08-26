from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title
