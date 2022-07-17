from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class index(APIView):

    def get(self, request):

        return Response({'success': True, 'message': 'Index Endpoint'}, status=status.HTTP_200_OK)


class Api_Endpoint(APIView):

    def get(self, request):

        return Response({'success': True, 'message': 'API Endpoint'}, status=status.HTTP_200_OK)