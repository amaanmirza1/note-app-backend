from django.contrib import admin
from django.urls import path, include

# JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 AUTH APIs (LOGIN + REFRESH TOKEN)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📝 NOTES API
    path('api/', include('notes.urls')),
]