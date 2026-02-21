from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from root.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
    # path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("admin/", admin.site.urls),
    path("api/v1/", include('apps.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_ROOT)