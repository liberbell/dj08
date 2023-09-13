from django.db import models

# Create your models here.
class Theme(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE
    )