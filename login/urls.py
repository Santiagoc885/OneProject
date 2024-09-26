from django.urls import path
from .views import ( 
    login,
    home
)

app_name = 'login'

urlpatterns = [
    path('', home.home, name='home'),
    path('login/', login.login, name='login'),
]
