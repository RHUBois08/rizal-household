from django.db import models
import uuid

class Household(models.Model):
    household_id = models.CharField(max_length=20, unique=True)
    person_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    barangay = models.CharField(max_length=100)
    purok = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)  # Increased length
    respondent = models.CharField(max_length=100)
    philhealth_member = models.BooleanField()
    philhealth_number = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.household_id
