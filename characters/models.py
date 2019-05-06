from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Section(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey('Section', blank=True, null=True, on_delete=models.CASCADE, related_name="belongs_section")

    def __str__(self):
        return self.name

class Entry(Section):
    general_desc = models.TextField(blank=True)
    belongs_to = models.ForeignKey('self', blank=True, null=True, related_name="belongs_entry", on_delete=models.CASCADE)


class Level(Entry):
    lvl = models.PositiveIntegerField()
    system_desc = models.TextField(blank=True, null=True)
    system_attribute = models.ForeignKey('Entry', blank=True, null=True, on_delete='CASCADE', related_name='attribute')
    system_ability = models.ForeignKey('Entry', blank=True, null=True, on_delete='CASCADE', related_name='ability')
    difficulty = models.CharField(max_length=150, blank=True, null=True, default='6')
