from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(10)])
    general_desc = models.TextField()
    system_desc = models.TextField()
    #system_attr = models.CharField(max_length=25)
    #system_attr = models.
    belongs_to= models.ForeignKey('self', null=True, related_name="belongs_to")

