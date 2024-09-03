from django.urls import path, include

from .custom_jwt_claims import CustomTokenObtainPairView

from users.views import UserView, NewUserView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),

    path('users/new', NewUserView.as_view(), name='new_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]