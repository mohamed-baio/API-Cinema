"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token 


router = DefaultRouter()
router.register('guests',views.Viewset_guest)
router.register('movies',views.Viewset_movie)
router.register('reservations',views.Viewset_reservation)


urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    #2
    path('django/jsonresponsewithmodel/', views.no_rest_from_model),
    #3.1
    path('rest/FBV_List/', views.FBV_List),
    #3.2
    path('rest/fbv/<int:pk>',views.FBV_pk),
    #4.1
    path('rest/cbv/',views.CBV_List.as_view()),
    #4.2
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    #5.1
    path('rest/mixins/',views.Mixins_list.as_view()),
    #5.2
    path('rest/mixins/<int:pk>',views.Mixins_pk.as_view()),
    #6.1
    path('rest/generics',views.Generics_list.as_view()),
    #6.2
    path('rest/generics/<int:pk>',views.Generics_pk.as_view()),
    #7.1
    path('rest/viewsets/', include(router.urls)),
    #8
    path('fbv/findmovie',views.find_movie),
    #9
    path('fbv/newreservation',views.new_reservation),
    #10
    path('api-auth',include('rest_framework.urls')),
    #11
    path('api-token-auth',obtain_auth_token),
    #12.1
    path('post/generics/<int:pk>',views.Post_pk.as_view()),
]
