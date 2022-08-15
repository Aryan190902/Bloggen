from django.urls import path
from .views import PassChangeView, ShowProfilePage, EditProfilePage, UserEdit, UserRegistration, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name="register"),
    path('edit_profile/', UserEdit.as_view(), name="editProfile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PassChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name="profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfilePage.as_view(), name="edit_profile_page"),
    path('create_profile_page/', CreateProfilePage.as_view(), name="create_profile_page"),
]
