from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from trex_chartist.apps.pattern_bank.api.serializer.dim_time_frame_serializer import DimTimeFrameSerializer
from trex_chartist.apps.pattern_bank.models import DimTimeFrame


class DimTimeFrameAPI(APIView):


    def get(self, request):
        models = DimTimeFrame.objects.all()
        serializer = DimTimeFrameSerializer(instance= models, many = True)

        return Response(serializer.data, status.HTTP_200_OK)
