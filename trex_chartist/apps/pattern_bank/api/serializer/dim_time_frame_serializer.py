from rest_framework import serializers

from trex_chartist.apps.pattern_bank.models import DimTimeFrame


class DimTimeFrameSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = DimTimeFrame