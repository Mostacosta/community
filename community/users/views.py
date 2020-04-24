from rest_framework.views import APIView
from .serializer import user_serializer,profile_serializer,contacts_serializer
from .models import user_profile,contacts
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from group.models import groups
import geopy.distance
from group.serializer import groups_serializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class user_api (APIView):
    def get(self, request,format=None):
        q = request.GET.get("q", None)
        if q:
            username = q
            user = User.objects.get(username = username)
            profile_ = user_profile.objects.get(user = user)
            serializer = contacts_serializer(profile_.contact,many=True)
            return Response (serializer.data)
        return Response("fe 7aga 4lt")
    def post (self,request,format=None):
        data = request.data
        if "password" in data :
            user = user_serializer(data=data)
            if user.is_valid():
                user = user.save()
                user.set_password(data["password"])
                user.save()
                return Response("user added")
            else:
                return Response(user.errors)
        else :
            contact_ = User.objects.get(username = data["username"])
            if contact_ :
                user = request.user
                user.user_profile.contact.add(user=contact_)
                return Response ("added")
            else :
                return Response ("no one with this name")

        return Response ("something went wrong ")

class location_api (APIView):
    permission_classes = [IsAuthenticated]
    def post (self,request,format=None):
        data = request.data
        print(data)
        long_ = data["longtude"]
        lat_ = data["latitude"]
        coords_1 = (long_, lat_)
        groups_ = groups.objects.all ()
        for group in groups_ :
            coords_2 = (group.longtude, group.latitude)
            dist = geopy.distance.geodesic(coords_1, coords_2).km
            if dist < 50 :
                serializer = groups_serializer(group)
                return Response (serializer.data)
        new_group = groups(name="new group",longtude=long_,latitude=lat_)
        new_group.save()
        return Response("new group")








    






