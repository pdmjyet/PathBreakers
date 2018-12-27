from django.db import models

class Profession(models.Model):
    # TODO
    # Tolower case
    name = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class ProfessionTag(models.Model):
    tag = models.CharField(max_length=30, unique=True, primary_key=True)
    profession = models.ManyToManyField(Profession)

    def __str__(self):
        return self.tag