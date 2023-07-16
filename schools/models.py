from django.contrib.gis.db import models


class School(models.Model):
    OBJECTID = models.IntegerField()
    CODE = models.CharField(max_length=50)
    SCHOOL_NAM = models.CharField(max_length=255)
    LEVEL = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    County = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    ZONE = models.CharField(max_length=50)
    SUBCOUNTY = models.CharField(max_length=50)
    Ward = models.CharField(max_length=50)
    X_Coord = models.FloatField()
    Y_Coord = models.FloatField()
    location = models.PointField()

    def __str__(self):
        return self.SCHOOL_NAM
