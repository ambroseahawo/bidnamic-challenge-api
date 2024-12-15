import datetime

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Form(models.Model):
    BIDS = (
        ("high", ("HIGH")),
        ("medium", ("MEDIUM")),
        ("low", ("LOW")),
    )

    title = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    dob = models.DateField()
    company_name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    telephone = PhoneNumberField(validators=[phone_regex], max_length=15, unique=True)
    bid = models.CharField(max_length=6, choices=BIDS)
    google_id = models.CharField(unique=True, max_length=10, validators=[MinLengthValidator(10)])
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # validate age before saving instance
    def save(self, *args, **kwargs):
        age = (datetime.date.today() - self.dob).days / 365
        if age < 18:
            raise ValidationError("You need to be at least 18 years old!")
        super(Form, self).save(*args, **kwargs)
