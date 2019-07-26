from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer, MainSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            password = serializer.validated_data.pop('password')
            user_profile = serializer.save()
            user_profile.set_password(password)
            user_profile.save()
        except:
            return Response({
                'message': '회원가입 오류'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'message': '회원가입 성공',
                'user_info': serializer.validated_data
            }, status=status.HTTP_201_CREATED)



class MainViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MainSerializer