"""codebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from backoffice import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'attributes', views.AttributeViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'managers', views.ManagerViewSet)
router.register(r'staffs', views.StaffViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'periods', views.PeriodViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'leagues', views.LeagueViewSet)
router.register(r'contracts', views.ContractViewSet)
router.register(r'games_videos', views.GameVideoViewSet)
router.register(r'playerspositions', views.PlayerPositionViewSet)
router.register(r'playeractioninGames', views.PlayerActionInGameViewSet)
router.register(r'teamexcel', views.TeamExcelViewSet, basename="teamexcel")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('get_password_reset_token/', views.get_password_reset_token),
    path('register/', views.register),
    path('active_account/', views.active_user_account),
    path('reset_password/', views.reset_password),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
