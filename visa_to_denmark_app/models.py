from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
