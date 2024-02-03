from django.db import models
from django.core.exceptions import ValidationError

def valid_age(val):
    if 10<=val<=100:
        return val
    else:
        raise ValidationError('Age limit exceeded!!')

def valid_pno(val):
    if len(str(val))==10:
        return val
    else:
        raise ValidationError('Invalid phone number!!')

class Data(models.Model):
    First_Name=models.CharField(max_length=50,null=False)
    Last_Name=models.CharField(max_length=50,null=False)
    Age=models.IntegerField(validators=[valid_age])
    Phone_Number=models.IntegerField(validators=[valid_pno])
    Email_ID=models.EmailField(max_length=30,null=False)
    Password=models.CharField(max_length=20,null=False)