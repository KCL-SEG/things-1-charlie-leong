from django.db import models
from enum import unique
from django.core.exceptions import ValidationError

def validate_number(value):
    if value < 0 or value >100:
        raise ValisationError("number must be between 0 and 100 (inclusive)")

class Thing(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 120, unique = False)
    quantity = models.IntegerField(validators = [validate_number])
