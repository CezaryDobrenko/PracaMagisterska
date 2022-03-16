from django.db import models

class Interval:
    class Options(models.TextChoices):
        MINUTE5 = "MINUTE5"
        MINUTE10 = "MINUTE10"
        MINUTE15 = "MINUTE15"
        MINUTE30 = "MINUTE30"
        MINUTE45 = "MINUTE45"
        HOUR1 = "HOUR1"
        HOUR2 = "HOUR2"
        HOUR3 = "HOUR3"
        HOUR6 = "HOUR6"
        HOUR12 = "HOUR12"
        DAY1 = "DAY1"
        DAY2 = "DAY2"
        DAY3 = "DAY3"
        DAY4 = "DAY4"
        DAY5 = "DAY5"
        DAY6 = "DAY6"
        WEEK = "WEEK"