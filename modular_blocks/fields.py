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

        # We delete empty values
        return [x for x in value.split(self.separator) if x != '']

    def get_prep_value(self, value):
        return self.separator.join(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([
        (
            [ListTextField],
            [],
            {
                "separator": ["separator", {"default": ","}],
            },
        ),
    ], ["^modular_blocks\.fields\.ListTextField"])
except ImportError:
    pass
