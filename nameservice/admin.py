from django.contrib import admin
from nameservice.models import NameServiceModel, UserPortalModel, PortalModel
# Register your models here.

admin.site.register(NameServiceModel) # Add to Admin Page
admin.site.register(PortalModel)
admin.site.register(UserPortalModel)