from rest_framework import serializers
from planapi.models import Company, GetPlans
# create serializers here


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = '__all__'


class Getplansserializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = GetPlans
        fields = "__all__"
