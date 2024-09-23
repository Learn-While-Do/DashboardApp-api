from django.urls import path, include

from .custom_jwt_claims import CustomTokenObtainPairView

from users.views import AdminResetUserPasswordView, DeactivateUserView,  ResetLoginAttemptsView, ResetUserPasswordView, UpdateUserStatusView, UpdateUserView, UserView, NewUserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),

    path('users/new', NewUserView.as_view(), name='new_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/deactivate', DeactivateUserView.as_view(), name='deactivate'),
    path('users/update-activity-status', UpdateUserStatusView.as_view(), name='update_activity_status'),
    path('users/update', UpdateUserView.as_view(), name='update_user'),
    path('users/admin-reset-login-attempts', ResetLoginAttemptsView.as_view(), name='unblock'),
    path('users/admin-reset-password', AdminResetUserPasswordView.as_view(), name='admin_reset_password'),
    path('users/user-reset-password',ResetUserPasswordView.as_view(), name='reset_password'),

]