from django.db import models


class Netcontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=15)
    popis = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'netcontypes'


class Hwtypes(models.Model):
    vendor_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)
    hw_profile = models.CharField(max_length=50)
    ports = models.IntegerField()
    shortname = models.CharField(max_length=10)
    def_wlan_freq = models.IntegerField(blank=True, null=True)
    def_wlan_ch_width = models.IntegerField(blank=True, null=True)
    def_wlan_antenna = models.IntegerField(blank=True, null=True)
    def_wlan_polarization = models.IntegerField(blank=True, null=True)
    oidmacvlanadr = models.CharField(max_length=100)
    oidmacvlandescr = models.CharField(max_length=100)
    oidmacvlanvlanid = models.CharField(max_length=100)
    oidmacvlanstatus = models.CharField(max_length=100)
    oidvlanid = models.CharField(max_length=100)
    oidvlandescr = models.CharField(max_length=100)
    oidvlanstatus = models.CharField(max_length=100)
    snmp_portconfig = models.TextField()

    class Meta:
        managed = False
        db_table = 'hwtypes'


class Nmsgroups(models.Model):
    name = models.CharField(max_length=150)
    notes = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmsgroups'


class Netdevices(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=255)
    description = models.TextField()
    producer = models.CharField(max_length=64)
    model = models.CharField(max_length=32)
    serialnumber = models.CharField(max_length=32)
    ports = models.IntegerField()
    purchasetime = models.IntegerField()
    guaranteeperiod = models.PositiveIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=32)
    nastype = models.IntegerField()
    clients = models.IntegerField()
    secret = models.CharField(max_length=60)
    community = models.CharField(max_length=50)
    channelid = models.IntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    hw_type = models.ForeignKey(Hwtypes, on_delete=models.DO_NOTHING, db_column='hw_type')
    nms_group = models.ForeignKey(Nmsgroups, on_delete=models.DO_NOTHING, db_column='nms_group')
    wlan_freq = models.IntegerField()
    wlan_ch_width = models.IntegerField()
    wlan_antenna = models.IntegerField()
    wlan_polarization = models.IntegerField()
    wlan_cipher = models.CharField(max_length=100, blank=True, null=True)
    netssid = models.CharField(max_length=32)
    con_type = models.ForeignKey(Netcontypes, on_delete=models.DO_NOTHING, db_column='con_type')

    class Meta:
        managed = False
        db_table = 'netdevices'
