from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from datetime import timedelta
# Create your models here.
def comma_separated_validator(value):
    items = value.split(',')
    for item in items:
        # Dummy validation: Ensure each item is at least 3 characters long
        if len(item.strip()) < 3:
            raise ValidationError(("Each item must be at least 3 characters long."))
class Dbproject(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField(default = 0)
    binary_field = models.BinaryField(default=b'\x01\x02\x03\x04')
    boolean_field = models.BooleanField(default=True)
    char_field = models.CharField(max_length=255,default='Fahim')
    comma_separated_field = models.CharField(
        validators=[comma_separated_validator],
        max_length=255,
        default='default,value,example' 
    )
    # date_field = models.DateField(default=date.today())
  
    


    def __str__ (self):
        return f'name: {self.char_field}'
    
class ModelOne(models.Model):
    generic_ip_address_field = models.GenericIPAddressField(default='192.168.1.1')
    float_field = models.FloatField(default=0.0)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2,default= 123.24)
    duration_field = models.DurationField(default=timedelta(days=7, hours=12, minutes=30))
    file_field = models.FileField(upload_to='files/', default='files/default_file.txt')

    


