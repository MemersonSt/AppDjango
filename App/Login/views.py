from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from App.Empleados.models import EmpleadoModel
from .serializers import LoginSerializer, TokenSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        correo = serializer.validated_data['Correo']
        password = serializer.validated_data['password']

        try:
            empleado = EmpleadoModel.objects.get(Correo=correo)
        except EmpleadoModel.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # if not check_password(password, empleado.password):
        #     return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        if (password != empleado.password):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(empleado)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'empleado': TokenSerializer(empleado).data
        }

        return Response(data, status=status.HTTP_200_OK)
