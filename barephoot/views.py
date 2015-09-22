from django.shortcuts import render
from django.http import HttpResponse
from barephoot.models import Movdata
from barephoot.models import Restdata
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from barephoot.serializers import Nserializer
from barephoot.serializers import Rserializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from django.contrib.auth.models import User
from barephoot.serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from barephoot.permissions import IsOwnerOrReadOnly



from django.views.decorators.csrf import csrf_exempt


def index(request):
    mov_list = Movdata.objects.all().order_by('id')[:3]
    context_dict = {'categories':mov_list}
    return render(request,'barephoot/index.html',context_dict)

def about(request):
    return HttpResponse("This is about my app")

@permission_classes((permissions.AllowAny,))
class MovList(APIView):
    """
    List all theatres, or create a new theatres.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        mov = Movdata.objects.all()
        serializer = Nserializer(mov, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Nserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@permission_classes((permissions.AllowAny,))
class MovDetail(APIView):
    """
    Retrieve, update or delete a Movdata instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def get_object(self, id):
        try:
            return Movdata.objects.get(id=id)
        except Movdata.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        mov = self.get_object(id)
        serializer = Nserializer(mov)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        mov = self.get_object(id)
        serializer = Nserializer(mov, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        mov = self.get_object(id)
        mov.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class ResList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self,request,format=None):
        res = Restdata.objects.all()
        serializer = Rserializer(res,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = Rserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@permission_classes((permissions.AllowAny,))
class ResDetail(APIView):
    """
    Retrieve, update or delete a Movdata instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def get_object(self, id):
        try:
            return Restdata.objects.get(id=id)
        except Restdata.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        res = self.get_object(id)
        serializer = Rserializer(res)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        res = self.get_object(id)
        serializer = Rserializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        res = self.get_object(id)
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

