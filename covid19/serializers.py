from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','name', 'total_confirmed_cases', 'total_deaths_cases', 'total_recovered_cases', 'date']
