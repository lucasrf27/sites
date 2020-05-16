from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from dealer.models import Car
from dealer.serializers import CarSerializer

class CarList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Car(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     cars = Car.objects.all()
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
