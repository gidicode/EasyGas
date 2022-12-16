from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [    
    path('login/', views.MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/completeRegistration/', views.CompleteUserRegistration.as_view(), name="complet_registration"),
    path('users/<int:pk>/editUser/', views.EditUser.as_view(), name="edit_user"),
    path('users/<int:pk>/changeProfilePicture/', views.ChangeProfilePicture.as_view(), name="change_profile_picture"),
    path('users/<int:pk>/changePassword/', views.ChangePassword.as_view(), name="change_password"),
    path("users/<int:pk>/updateVendorProfile", views.UpdateVendorRegComplete.as_view(), name = "update_vendor_profile")
]

urlpatterns = format_suffix_patterns(urlpatterns)