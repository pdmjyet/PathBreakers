from django.db import models

class Profession(models.Model):
    # TODO
    # Tolower case
    name = models.CharField(max_length=30, unique=True, primary_key=True)