from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Entry(models.Model):
    name = models.CharField(max_length=25)
    minLevel=0
    maxLevel=10
    level = models.PositiveIntegerField(null=True,validators=[MinValueValidator(minLevel), MaxValueValidator(maxlevel)])
    general_desc = models.TextField()

    def __str__(self):
        return self.name

    def increaseLevel(self,increase):
        self.level = self.level + increase
        if self.level > self.maxLevel:
            self.level= self.maxLevel

    def decreaseLevel(self, decrease):
        self.level = self.level - decrease
        if self.level < self.minLevel:
            self.level = self.minLevel


