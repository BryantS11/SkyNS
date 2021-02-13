from django.urls import path
from nameservice import views
#

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("create", views.SkyNSCreateView.as_view(), name="nsCreate"),
    path("list", views.SkyNSListView.as_view(), name="nsList"),
    path("update/<int:pk>", views.SkyNSUpdateView.as_view(), name="nsUpdate"),
    path("detail/<int:pk>", views.SkyNSDetailView.as_view(), name="nsDetail"),
    path("delete/<int:pk>", views.SkyNSDeleteView.as_view(), name="nsDelete"),
]
