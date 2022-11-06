from django.db import models

# Create your models here.
class Card(models.Model):
    card_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 50)
    phase = models.CharField(max_length = 50)

    def __str__(self):
        return self.title