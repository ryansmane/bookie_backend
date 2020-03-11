from .models import Agent, Agency
from rest_framework import viewsets, permissions
from .serializers import AgentSerializer, AgencySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics, authentication

from rest_framework import status



class AgentList(APIView):
    
    def get(self, request, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Missing Fields")

class AgencyList(APIView):
    
    def get(self, request, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        Agencies = Agency.objects.all()
        serializer = AgencySerializer(Agencies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        serializer = AgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Invalid Information')

class AgentDetail(APIView):

    def get_object(self, identity):
        authentication_classes = [authentication.TokenAuthentication]
        return Agent.objects.get(identity=identity)
        

    def get(self, request, identity, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        snippet = self.get_object(identity)
        serializer = AgentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, identity, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        snippet = self.get_object(identity)
        serializer = AgentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgencyDetail(APIView):

    def get_object(self, pk):
        authentication_classes = [authentication.TokenAuthentication]
        return Agency.objects.get(pk=pk)
        

    def get(self, request, pk, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        snippet = self.get_object(pk)
        serializer = AgencySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        snippet = self.get_object(pk)
        serializer = AgencySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


