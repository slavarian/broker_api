from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from auths.views import UserViewSet
from companyshares.views import CompanyViewSet , SharesViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)

company_router = DefaultRouter()
company_router.register(r'list', CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
    path('company/',include(company_router.urls)),
    path("auth/", include("auths.urls")),
]

urlpatterns += [
 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]