from django.urls import path
from users import views


urlpatterns=[
    path('register/',views.SignupView.as_view(),name='signup'),
    path('login/',views.SigninView.as_view(),name='signin'),
]