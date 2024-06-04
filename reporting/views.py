from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from reporting.models import Order
from reporting.serializers import OrderSerializer

class ReportingViewSet(APIView):
    def get(self, request):

        answer = {'id': "42", 'name': "question"}

        return Response(answer)
        
class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-created_time')