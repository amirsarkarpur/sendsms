from django.db import models
from django.core.validators import RegexValidator


class give_data (models.Model):

    first_name = models.CharField(blank=False,null=False,max_length=80)
    last_name = models.CharField(blank=False,null=False,max_length=80)
    phone_number = models.CharField(
        max_length=11,
        unique=False,
        validators=[
            RegexValidator(r'^09\d{9}$', 'شماره موبایل باید با 09 شروع شود و 11 رقم باشد.')
        ]
    )

    def __str__(self) :
        name = self.first_name +" "+ self.last_name
        return name
