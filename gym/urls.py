from django.urls import path
from .views import index,admin_panel,signIn,api_update

urlpatterns = [
    path('',index ,name='index'),
    path('login',signIn,name='login'),
    path('painel/portaria',admin_panel,name='admin_panel'),
    path('panel/portaria/update/<int:id>',api_update,name='api'),
]