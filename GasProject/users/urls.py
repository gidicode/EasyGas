from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [    
    path('login/', views.MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('users/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)