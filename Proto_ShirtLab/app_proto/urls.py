from django.conf.urls import url
from app_proto import views

app_name = 'app_proto'

urlpatterns = [
    url(r'^user/', views.sl_users,name='users'),
    url(r'^signup/', views.signup,name='signup'),
    url(r'^registration/', views.registration,name='registration'),
    url(r'^user_login/', views.user_login,name='user_login'),

]
