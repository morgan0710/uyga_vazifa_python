from django.contrib import admin
from django.urls import path
from app.views import ProtectedDataView, SignupView, LogoutView

urlpatterns = [
    path('login/', ProtectedDataView.as_view(), name='protected-data'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]