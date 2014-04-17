from django.views import generic
from django.contrib.auth import get_user_model

from .forms import ModularChangeForm


class ModularChangeView(generic.UpdateView):
    model = get_user_model()
    form_class = ModularChangeForm
    template_name = "modular_blocks/sidebars.html"
    
    def get_object(self, *args, **kwargs):
        return self.request.user


