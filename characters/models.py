from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Section(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey('Section', blank=True, null=True, on_delete=models.CASCADE, related_name="belongs_section")

    def __str__(self):
        return self.name

class Entry(Section):
    minLevel=0
    maxLevel=10
    #level = models.PositiveIntegerField(validators=[MinValueValidator(minLevel), MaxValueValidator(maxLevel)], default=1)
    #models.ForeignKey('Level', blank=True, null=True, related_name="belongs_entry", on_delete=models.CASCADE)

    general_desc = models.TextField(blank=True)
    belongs_to = models.ForeignKey('self', blank=True, null=True, related_name="belongs_entry", on_delete=models.CASCADE)



    def increase_level(self,increase):
        self.level = self.level + increase
        if self.level > self.maxLevel:
            self.level= self.maxLevel

    def decrease_level(self, decrease):
        self.level = self.level - decrease
        if self.level < self.minLevel:
            self.level = self.minLevel


class Level(Entry):
    number = models.PositiveIntegerField()
    system_desc = models.TextField(blank=True, null=True)
    system_attribute = models.ForeignKey('Entry', blank=True, null=True, on_delete='CASCADE', related_name='attribute')
    system_ability = models.ForeignKey('Entry', blank=True, null=True, on_delete='CASCADE', related_name='ability')
    difficulty = models.PositiveIntegerField(blank=True, null=True,default=6)