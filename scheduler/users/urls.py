from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views as users

app_name = "users"

urlpatterns = [
    path("", users.UserView.as_view(), name="user_list"),
    path("user_get/", RedirectView.as_view(url="/api/users")),
    path("user_get/<int:id>", users.SingleUserView.as_view()),
    path("user_post", users.SingleUserView.as_view()),
    path("user_post/<int:id>", users.SingleUserView.as_view(), {"method": "patch"}),
]
