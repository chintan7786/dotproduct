from django.db import models

PHASE_CHOICES = (
    ('TO-DO', 'TO-DO'),
    ('Doing', 'Doing'),
    ('Done', 'Done')
)

# Create your models here.
class Card(models.Model):
    card_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 50)
    phase = models.CharField(max_length = 50)
    # step = models.CharField(choices = PHASE_CHOICES ,max_length = 50, blank=True, null=True)

    def __str__(self):
        return self.title