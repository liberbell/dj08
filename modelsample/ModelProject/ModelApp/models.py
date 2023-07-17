from django.db import models
from django.utils import timezone
import pytz

# Create your models here.

class BaseMeta(models.Model):
    create_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone("Asia/Tokyo")))
    update_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone("Asia/Tokyo")))

    class Meta:
        abstract = True

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    momo = models.TextField()
    web_site = models.URLField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)

    class Meta:
        db_table = 'person'
        index_together = [["first_name", "last_name"]]
        ordering = ["salary"]