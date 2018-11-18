from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from .PersonalInfo import PersonalInfo
from .Profession import  Profession


def YOGValidator(yog):
    if len(yog) != 9 or '-' not in yog:
        raise ValidationError('invalid year of graduation')
    years = yog.split('-')
    if int(years[0]) >= int(years[1]):
        raise ValidationError('invalid year of graduation range')


class PathBreaker(PersonalInfo):
    yog = models.CharField(max_length=9,
                           validators = [
                                RegexValidator(
                                    regex = '^[1-9][0-9]{3}-[1-9][0-9]{3}$',
                                    message = 'invalid year of graduation',
                                    code = 'invalid_yog'
                                    ),
                                YOGValidator
                            ])
    Profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

