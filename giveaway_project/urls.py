from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from giveaways import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="giveaways/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.signup, name="signup"),
    path("", views.home, name="home"),
    path("giveaway/", include("giveaways.urls")),
]
