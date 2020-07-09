"""restapi URL Configuration

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
from django.urls import path
from apis import views
from apis import fun
from django.conf.urls import include

from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
        # path('', include(router.urls)),
        # path('create_post/',fun.list_fun),
        # path('post_view/',fun.post_view),
        # path('addview/',fun.addview),
        path('user/all/',fun.All_User),
        # path('user/<int:pk>/', views.UserDetail.as_view()),
path('login_view/',views.login_view ),
path('dashbord/',views.dashbord ),
path('user/<int:pk>/',fun.user_detailes),
    path('reg_view/',fun.reg_view),
    path('reguser/',fun.addreg),
    # path('createuser/', views.CreateUser.as_view()),

path('users/', views.UserList.as_view()),
path('userset/', views.UserViewSet.as_view()),
path('setpassword/', views.ChangePasswordView.as_view()),
    path(r'oauth/', include('social_django.urls', namespace='social')),  # <--


# path('users/<int:pk>/', views.UserDetail.as_view()),
]
