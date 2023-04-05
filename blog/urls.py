"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.posts.views import PostAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView
from apps.users.views import UserAPIView, RegisterAPIView, UserUpdateAPIView, UserDeleteAPIView
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
#     patterns=[path('api/', include('myapi.urls')), ],
#     public=True,
#     permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/posts/', PostAPIView.as_view(), name = "api_posts"),
    path('api/posts/create/', PostCreateAPIView.as_view(), name="api_post_create"),
    path('api/posts/update/<int:pk>', PostUpdateAPIView.as_view(), name="api_posts_update"),
    path('api/posts/delete/<int:pk>', PostDeleteAPIView.as_view(), name="api_delete_view"),
    path('api/users/', UserAPIView.as_view(), name="api_users"),
    path('api/users/register/', RegisterAPIView.as_view(), name='api_users_register'),
    path('api/users/update/<int:pk>/', UserUpdateAPIView.as_view(), name="api_users_update"),
    path('api/users/delete/<int:pk>/', UserDeleteAPIView.as_view(), name="api_users_delete"),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_refresh"),
    path('api/login/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)