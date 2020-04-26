from django.db import models

# Create your models here.
class RankList(models.Model):
    port_id = models.IntegerField(null=False)
    title = models.CharField(max_length=32,null=False)
    score = models.PositiveIntegerField()
