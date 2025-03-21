from django.db import models


class DimDate(models.Model):
    date = models.DateField(primary_key=True)

    monthId = models.SmallIntegerField(null=False, blank=False)
    dayOfWeek = models.SmallIntegerField(null=False, blank=False)
    dayOfMonth = models.SmallIntegerField(null=False, blank=False)
    dayOfYear = models.SmallIntegerField(null=False, blank=False)

    isWorkingDay = models.BooleanField(null=False, blank=False)
    # isHoliday = models.BooleanField(editable= False,null=False, blank= False)


class DimTime(models.Model):
    time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return str(self.time)


class DimSymbol(models.Model):
    symbolName = models.CharField(max_length=8)

    def __str__(self):
        return self.symbolName


class DimTimeFrame(models.Model):
    timeFrameName = models.CharField(max_length=4, )
    m1Count = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.timeFrameName


class DimCandle(models.Model):
    open = models.FloatField(null=False, blank=False, editable=False)
    close = models.FloatField(null=False, blank=False, editable=False)
    high = models.FloatField(null=False, blank=False, editable=False)
    low = models.FloatField(null=False, blank=False, editable=False)
    volume = models.IntegerField(null=False, blank=False, editable=False)
    rangePips = models.IntegerField(null= False, blank= False, editable=False)

    atr16 = models.FloatField(null=True, blank=True)
    atrTrex = models.FloatField(null=True, blank=True)
    rsi = models.FloatField(null=True, blank=True)

    candleColor = models.CharField(max_length=1,
                                   choices=[('g', 'green'), ('e', 'equal'), ('r', 'red')],
                                   null=False,
                                   blank=False)

    date = models.ForeignKey(DimDate, on_delete=models.PROTECT, null=False, blank=False, editable=False)
    time = models.ForeignKey(DimTime, on_delete=models.PROTECT, null=False, blank=False, editable=False)
    symbol = models.ForeignKey(DimSymbol, on_delete=models.PROTECT, null=False, blank=False, editable=False)
    timeFrame = models.ForeignKey(DimTimeFrame, on_delete=models.PROTECT, null=False, blank=False, editable=False)

    def __str__(self):
        return f'{self.date.date} {self.time} , {self.timeFrame}'


class DimPatternGroup(models.Model):
    patternGroupName = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.patternGroupName


class DimPatternType(models.Model):
    patternGroup = models.ForeignKey(DimPatternGroup, on_delete=models.PROTECT)
    patternName = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.patternName


class FactPattern(models.Model):
    patternType = models.ForeignKey(DimPatternType, on_delete=models.PROTECT, null=True, blank=True)

    timeFrame = models.ForeignKey(DimTimeFrame, on_delete=models.PROTECT, related_name='structTimeFramePatterns')
    triggerTimeFrame = models.ForeignKey(DimTimeFrame, on_delete=models.PROTECT,
                                         related_name='triggerTimeFramePatterns')

    startCandle = models.ForeignKey(DimCandle, on_delete=models.PROTECT, related_name='startPatterns')
    endCandle = models.ForeignKey(DimCandle, on_delete=models.PROTECT, related_name='endPatterns')
