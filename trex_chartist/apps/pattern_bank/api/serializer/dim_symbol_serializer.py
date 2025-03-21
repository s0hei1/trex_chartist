from rest_framework import serializers

from trex_chartist.apps.pattern_bank.models import DimSymbol


class DimSymbolSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = DimSymbol