from django.db import models

# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        abstract = True

class Books(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)