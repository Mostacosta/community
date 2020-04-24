from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import groups_serializer,posts_serializer,comments_serializer
from .models import groups,posts,comments
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

# Create your views here.

class group_contacts (APIView):
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    def get (self, request,format=None):
        q = request.GET.get('q',None)
        if q :
            contacts = []
            group = get_object_or_404(groups,pk=int(q))
            posts_ = posts.objects.filter(group=group)
            print(posts_)
            for post in posts_ :
                comment = comments.objects.filter (post=post)
                print(comment)
                if comment:
                    serilizer = comments_serializer(comment,many=True)
                    contacts.append(serilizer.data)
            return Response (contacts)
        return Response ("fe 7aga 4lt")

    def post (self, request,format=None):
        data = request.data 
        if "post" in data :
            serializer = posts_serializer(data=data)
            if serializer.is_valid():  
                serializer.save(user = request.user, group = groups.object.get(pk=int(data["group"])) )
            else:
                return Response(serializer.errors)
        else :
            serializer = comments_serializer(data=data)
            if serializer.is_valid():  
                serializer.save(user = request.user, post = groups.object.get(pk=int(data["post"])) )
            else:
                return Response(serializer.errors)
        return Response("done")
    
    def delete(self, request, format=None):
        q = request.GET.get("q")
        snippet = posts.objects.get(pk=int(q))
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put (self, request,format=None):
        data = request.data
        group_ = groups.object.get(pk=data["id"])
        group_.name = data["name"]
        group_.save() 
        return Response("updated")
    



