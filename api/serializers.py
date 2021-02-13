from nameservice.models import NameServiceModel
from rest_framework import serializers
#

# Serializers define the API representation.
class SkyNSSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Get request.user

    class Meta:
        model = NameServiceModel
        fields = ['user', 'name', 'skylink']
