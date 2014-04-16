from django.db import models


class ListTextField(models.TextField):
    description = "An field representing an array"

    __metaclass__ = models.SubfieldBase

    def __init__(self, separator=',', *args, **kwargs):
        self.separator = separator
        super(ListTextField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return value.split(self.separator)

    def get_prep_value(self, value):
        return self.separator.join(value)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([
    (
        [ListTextField],
        [],
        {
            "separator": ["separator", {"default": ","}],
        },
    ),
], ["^modulable_app\.fields\.ListTextField"])
