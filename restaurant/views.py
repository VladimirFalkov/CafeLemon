from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer




# Create your views here.
def index(request):
 return render(request, 'index.html', {})


class BookingView(APIView):

    def get(self, request):
       items = Booking.objects.all()
       serializer = BookingSerializer(items, many=True)
       return Response(serializer.data) # REturn JSON
    

class MenuView(APIView):
   def post(self, request):
      serializer = MenuSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'status':'sucess', 'data': serializer.data})

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
   return Response({"message":"This view is protected"})