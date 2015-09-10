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
        if isinstance(user.topbar, list):
            blocks_names += user.topbar
        elif user.topbar is not None:
            blocks_names += [user.topbar]

        nub = modules.get_non_used_blocks(*blocks_names)
        mid = len(nub)/2
        cd['non_used_blocks_1'] = nub[:mid]
        cd['non_used_blocks_2'] = nub[mid:]

        return cd
