from django.db import models

class Profession(models.Model):
    # TODO
    # Tolower case
    name = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    # TODO
    # Tolower case
    tag = models.CharField(max_length=30, unique=True, primary_key=True)

    def __str__(self):
        return self.tag


class ProfessionTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)
    #tag = models.CharField(max_length=30, unique=True, primary_key=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('tag', 'profession',)

    def __str__(self):
        return self.tag.tag + self.profession.name