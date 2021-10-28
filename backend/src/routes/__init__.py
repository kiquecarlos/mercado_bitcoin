from django.urls import path
from backend.src.controllers.mms import MMSController


urlpatterns = [
    path('mms/<str:pair>/', MMSController.as_view({'get': 'index'})),
]
