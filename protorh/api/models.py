from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    firstname = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    email = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'users'
