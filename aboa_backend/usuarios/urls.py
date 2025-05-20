from django.urls import path
from . import views
from .views import cadastro_estabelecimento
from .views import LoginRestauranteView
from .views import home_comercio
from .views import logout_view


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('recomendacoes/', views.recomendacoes, name='recomendacoes'),
    path('cadastro-comercio/', cadastro_estabelecimento, name='cadastro_comercio'),
    path('login-restaurante/', LoginRestauranteView.as_view(), name='login_restaurante'),
    path('home-comercio/', home_comercio, name='home_comercio'),
    path('logout/', logout_view, name='logout'),
    
]
