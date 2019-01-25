"""workouts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from plans.views import \
    (ExerciseViewSet,DaysViewSet,WorkoutPlanViewSet,
     UserViewSet,UserPlanViewSet,PlanDaysDetailsViewSet,PlanExerciseDetailsViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'exercise', ExerciseViewSet, base_name='excercise')
router.register(r'days', DaysViewSet, base_name='days')
router.register(r'plan', WorkoutPlanViewSet)
router.register(r'user', UserViewSet)
router.register(r'userplan', UserPlanViewSet)
router.register(r'plandaysdetails', PlanDaysDetailsViewSet)
router.register(r'planexercisedetails', PlanExerciseDetailsViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls

