import datetime

from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from source.models import Images, Persons
from source.serializers import ImageSerializer, ImageSerializerList, PersonSerializer


class ImagesAPIListView(APIView):

    def get(self, request, pk=None):
        if pk:
            images_list = get_object_or_404(Images, pk=pk)
            serializer_data = ImageSerializerList(images_list)
        else:
            images_list = Images.objects.all()
            serializer_data = ImageSerializerList(images_list, many=True)

        return Response({'images': serializer_data.data})

    def post(self, request):
        serializer_data = ImageSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()

        return Response({'status': 201})

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


class ImageFilterView(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class = ImageSerializerList

    def get_queryset(self):
        queryset = None
        if 'geolocation' in self.request.query_params:
            queryset = Images.objects.filter(geolocation=self.request.query_params['geolocation'])
        elif 'created_at' in self.request.query_params:
            try:
                created_at = datetime.datetime.strptime(self.request.query_params['created_at'], "%Y-%m-%d %H:%M:%S")
            except Exception as e:
                print(e)
                created_at = datetime.datetime.strptime(self.request.query_params['created_at'], "%Y-%m-%d").date()
            queryset = Images.objects.filter(created_at__startswith=created_at)
        elif 'persons_names' in self.request.query_params:
            queryset = Images.objects.filter(persons_names__name=self.request.query_params['persons_names'])
        return queryset


class PeopleNameSearchView(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = None
        if 'persons_names' in self.request.query_params:
            queryset = Persons.objects.filter(name__istartswith=self.request.query_params['persons_names'])
        return queryset
