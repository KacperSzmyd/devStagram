from django.urls import path
from .views import ProfileListView, ProfileView, loginPage, logoutUser, SignUpView

urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
    path('profile/<uuid:pk>/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout')
]