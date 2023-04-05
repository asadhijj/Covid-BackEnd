from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer


class CountryRecordListCreateAPIView(APIView):
    """
    List all countries or create a new country record
    """
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryRecordRetrieveDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response({'error': 'Country does not exist'}, status=status.HTTP_404_NOT_FOUND)

        country.delete()
        return Response({'success': 'Country deleted successfully'}, status=status.HTTP_204_NO_CONTENT)