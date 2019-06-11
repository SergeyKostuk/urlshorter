import string

from django.db import models
from random import choice
def generate_url():
    chars = string.digits
    return ''.join(choice(chars) for _ in range(3))
class Url(models.Model):
    long_url= models.URLField()
    short_url = models.CharField(max_length=300,default=generate_url)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    count = models.PositiveIntegerField(default=0)
# Create your models here.
