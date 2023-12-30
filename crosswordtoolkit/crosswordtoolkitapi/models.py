from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password_salted_hash = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.username


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Crossword(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateTimeField("Date published")
    num_rows = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.publisher}: {self.publication_date}"
