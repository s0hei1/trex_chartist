from rest_framework import serializers
from trex_chartist.apps.pattern_bank.models import DimTime


class DimTimeSerializer(serializers.Serializer):
    time = serializers.TimeField(format="%H:%M")
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DimTime
        fields = ['id','time']


    def create(self, validated_data):

        return DimTime.objects.create(**validated_data)