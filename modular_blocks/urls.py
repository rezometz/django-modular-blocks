from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import ModularChangeView


urlpatterns = patterns('',
    url(
        r'^change$',
        login_required(ModularChangeView.as_view()),
        name="modular-change",
    ),

)
