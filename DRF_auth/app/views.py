from rest_framework import ApiView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, permissions
from .serializers import *
from rest_framework import status

class ProtectedView(ApiView):

    def get(self, request):
        context = {
            'status': 'Muvaffaqiyatli',
            'message': 'Siz BasicAuthentication orqali himoyalangan API ga kirdingiz!'
            'user': request.user.username,
            'email': request.user.email,
        }
        return Response(context)

    class SignupView(generics.CreateAPIView):
    """
    Ro`yxatdan o`tish uchun ochiq endpoint - autentifikatsiya talab qilinmaydi. 
    """
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [] # signup uchun auth shart emas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
            "message": "Muvaffaqiyatli ro`yxatdan o`tildi.",
            'username': user.username,
        }
        status=status.HTTP_201_CREATED,
        )

class LogoutView(APIView):
    """
    Sessiyani tugatish (SessionAuthentication ishlatilganda).
    BasicAuthentication uchun esa client tomonda
    saqlangan username/parolni o`chirish kifoya.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Tizimdan muvaffaqiyatli chiqdingiz.'})