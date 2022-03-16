from django.db import models

class Level:
    class Options(models.TextChoices):
        FREE = "FREE"
        PREMIUM = "PREMIUM"