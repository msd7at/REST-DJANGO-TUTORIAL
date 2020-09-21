from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class PersonViewPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3


class PersonView(generics.ListAPIView):
    # GET
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', "Name")
    search_fields = ('id', "Name")
    pagination_class = PersonViewPagination


class PersonRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    lookup_field = 'id'
    serializer_class = PersonSerializer

    def delete(self, request, *args, **kwargs):
        try:
            id = request.data.get('id', None)
            response = super().delete(request, *args, **kwargs)
            if response.status_code == 204:
                from django.core.cache import cache
                cache.delete("{}".format(id))
                return response
        except Exception as e:
            return(
                {
                    "Message": "Failed"
                }
            )

    def update(self, request, *args, **kwargs):
        response=super().update(request,*args, **kwargs)
        if response.status_code==200:
            mydata= response.data
            from django.core.cache import cache
            cache.set("ID:".format(mydata.get('id',None))
            {"name":mydata['name'],
            "age":mydata["age"],
            'birthday':mydata['birthday']
            })
        return response

# class PersonView(APIView):
#     def get(self,request,format=None):
#         data=Person.objects.all()
#         print("dasdsa",data)
#         serializer = PersonSerializer(data,many=True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         try:
#             serializer=PersonSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


"""
# # Create your views here.
# # def index(request):
# #     return HttpResponse("<H1>Hellow woeldfD</H1>" )
# class Youtube(APIView):
#     def __init__(self):
#         self.data=["anurag"]
#     def get(self,requests,format=None):
#         return Response({"संदेश ":self.data})
#     def post(self,requests,format=None):
#         data=requests.data  
#         Name=data.get("Name",None)
#         self.data.append(Name)
#         return Response(

#             {"Response":200,
#             "Data":Name,
#             "Message":"it was added to db"}
#        
"""
