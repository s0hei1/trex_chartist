from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from trex_chartist.apps.pattern_bank.models import DimSymbol, DimDate, DimTimeFrame, DimCandle, DimTime, \
    DimPatternGroup, DimPatternType, FactPattern


class DimDateResource(resources.ModelResource):
    class Meta:
        model = DimDate
        import_id_fields = ['date']

class DimCandleResource(resources.ModelResource):
    class Meta:
        model = DimCandle

    def before_import_row(self, row, **kwargs):

        symbolId = DimSymbol.objects.filter(symbolName=row['symbol']).first().id
        row['symbol'] = symbolId

        timeId = DimTime.objects.filter(time=row['time']).first().id
        row['time'] = timeId

        tfId = DimTimeFrame.objects.filter(timeFrameName =row['timeFrame']).first().id
        row['timeFrame'] = tfId



@admin.register(DimSymbol)
class DimSymbolAdmin(admin.ModelAdmin):
    list_display = ['symbolName' , 'id']

@admin.register(DimTimeFrame)
class DimTimeFrameAdmin(admin.ModelAdmin):
    list_display = ['timeFrameName' , 'id' ,'m1Count']

@admin.register(DimDate)
class DimDateAdmin(ImportExportModelAdmin):
    resource_class = DimDateResource

@admin.register(DimCandle)
class DimCandleAdmin(ImportExportModelAdmin):
    resource_class = DimCandleResource

@admin.register(DimTime)
class DimTimeAdmin(admin.ModelAdmin):
    list_display = ['time' , 'id' ]

@admin.register(DimPatternGroup)
class DimPatternGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(DimPatternType)
class DimPatternTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(FactPattern)
class FactPatternAdmin(admin.ModelAdmin):
    pass



