from django import forms
from django.contrib.auth import get_user_model


class HiddenListInput(forms.HiddenInput):
    def _format_value(self, value):
        return ','.join(value)


class ModularChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'sidebar_left',
            'sidebar_right',
            'topbar',
        )
        widgets = {
            'sidebar_left': HiddenListInput(),
            'sidebar_right': HiddenListInput(),
            'topbar': HiddenListInput(),
        }
