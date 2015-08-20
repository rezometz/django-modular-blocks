from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ModularChangeView


urlpatterns = [
    url(
        r'^change$',
        login_required(ModularChangeView.as_view()),
        name="modular-change",
    ),

]
