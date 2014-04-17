from django.views import generic
from django.contrib.auth import get_user_model

from modular_blocks import modules

from .forms import ModularChangeForm


class ModularChangeView(generic.UpdateView):
    model = get_user_model()
    form_class = ModularChangeForm
    template_name = "modular_blocks/sidebars.html"
    
    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        cd = super(ModularChangeView, self).get_context_data(*args, **kwargs)
        user = self.request.user 

        blocks_names = user.sidebar_left + user.sidebar_right

        cd['non_used_blocks'] = modules.get_non_used_blocks(*blocks_names)

        print cd['non_used_blocks']

        return cd

