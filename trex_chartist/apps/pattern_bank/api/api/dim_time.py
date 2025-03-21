from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from trex_chartist.apps.pattern_bank.api.serializer.dim_time_serializer import DimTimeSerializer
from trex_chartist.apps.pattern_bank.models import DimTime


class DimTimeApi(APIView):

    @swagger_auto_schema(
        request_body=DimTimeSerializer,
        responses={201: DimTimeSerializer, 400: "Bad Request"},
    )
    def post(self, request):
        serializer = DimTimeSerializer(data=request.data, many= True)  # Ensure many=True only if data is a list

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        models = DimTime.objects.all()
        serializer = DimTimeSerializer(instance= models, many = True)

        return Response(serializer.data, status.HTTP_200_OK)


