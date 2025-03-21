from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from trex_chartist.apps.pattern_bank.api.serializer.dim_symbol_serializer import DimSymbolSerializer
from trex_chartist.apps.pattern_bank.models import DimSymbol


class DimSymbolAPI(APIView):

    def get(self, request):
        models = DimSymbol.objects.all()
        serializer = DimSymbolSerializer(instance= models, many = True)

        return Response(serializer.data, status.HTTP_200_OK)
