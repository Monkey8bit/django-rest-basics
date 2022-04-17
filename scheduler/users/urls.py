from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from . import views as users

app_name = "users"

urlpatterns = [
    path("", users.UserView.as_view(), name="user_list"),
    path("<int:id>", users.SingleUserView.as_view()),
    path("<int:id>", users.SingleUserView.as_view(), {"method": "patch"}),
]
