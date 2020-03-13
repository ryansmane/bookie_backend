from rest_framework import status, permissions, generics, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import User
from .serializers import RegisterSerializer, UserSerializer, TokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

@api_view(['POST',])
@permission_classes([AllowAny],)
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['email'] = account.email
            data['username'] = account.username
            data['boolean'] = account.is_agent
            data['id'] = account.id
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@permission_classes([AllowAny],)
class Login(APIView):
    throttle_classes = ()
    # permission_classes = [AllowAny]
    
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class TokenDetail(APIView):
    """
    View to list all Tokens in the system.

    * Requires token authentication.
    * Only admin Tokens are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    
    

    def get_object(self, key):
        
            return Token.objects.get(key=key)
        

    def get(self, request, key, format=None):
        snippet = self.get_object(key)
        serializer = TokenSerializer(snippet)
        return Response(serializer.data)




class UserDetail(APIView):


    def get_object(self, pk):
        
            return User.objects.get(pk=pk)
        

    def get(self, request, pk, format=None):
        authentication_classes = [authentication.TokenAuthentication]
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


