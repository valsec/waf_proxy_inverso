from django.db import models

class Systemevents(models.Model):
    customerid = models.BigIntegerField(blank=True, null=True)
    receivedat = models.DateTimeField(blank=True, null=True)
    devicereportedtime = models.DateTimeField(blank=True, null=True)
    facility = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    fromhost = models.CharField(max_length=60, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    ntseverity = models.IntegerField(blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    eventsource = models.CharField(max_length=60, blank=True, null=True)
    eventuser = models.CharField(max_length=60, blank=True, null=True)
    eventcategory = models.IntegerField(blank=True, null=True)
    eventid = models.IntegerField(blank=True, null=True)
    eventbinarydata = models.TextField(blank=True, null=True)
    maxavailable = models.IntegerField(blank=True, null=True)
    currusage = models.IntegerField(blank=True, null=True)
    minusage = models.IntegerField(blank=True, null=True)
    maxusage = models.IntegerField(blank=True, null=True)
    infounitid = models.IntegerField(blank=True, null=True)
    syslogtag = models.CharField(max_length=60, blank=True, null=True)
    eventlogtype = models.CharField(max_length=60, blank=True, null=True)
    genericfilename = models.CharField(max_length=60, blank=True, null=True)
    systemid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systemevents'


class Systemeventsproperties(models.Model):
    systemeventid = models.IntegerField(blank=True, null=True)
    paramname = models.CharField(max_length=255, blank=True, null=True)
    paramvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systemeventsproperties'
