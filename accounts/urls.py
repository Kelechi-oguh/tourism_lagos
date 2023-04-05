from django.urls import path

from .views import SignUpView, LogInView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
