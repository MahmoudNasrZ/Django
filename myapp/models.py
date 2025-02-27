from django.db import models

# Create your models here.
# class BaseModel(models.Model):
#    ceated_at= models.DateTimeField(auto_now_)
class ClassRoom(models.Model):
    name = models.CharField(verbose_name="Class Name", max_length=50, unique=True)
    subject = models.CharField(verbose_name="Subject", max_length=50)
    year = models.IntegerField(verbose_name="Year")

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.year})"

class ClassArea(models.Model):
    length = models.IntegerField(verbose_name="Class Length")
    width = models.IntegerField(verbose_name="Class Width")

    def __str__(self):
        return f"Class Area: {self.length} x {self.width}"
