from rest_framework import viewsets
from api.serializers import SkyNSSerializer
from nameservice.models import NameServiceModel
# Create your views here.

# ViewSets define the view behavior.


class SkyNSViewSet(viewsets.ModelViewSet):
    queryset = NameServiceModel.objects.all()
    serializer_class = SkyNSSerializer