from django.db import models

class Article(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default=None, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantite = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return self.name

