from django.urls import path

from measurement.views import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', ListCreateAPIView.as_view()),
]