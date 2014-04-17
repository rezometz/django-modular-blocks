from django import template
from django.template.base import (Node, InvalidTemplateLibrary, get_library)

from .. import modules, ModuleApp, BlockDoesNotExist


register = template.Library()


class RenderModuleNode(Node):
    def __init__(self, parser, context_variable_name):
        self.parser = parser
        self.module_name = template.Variable(context_variable_name)

    def load_library_for(self, block):
        try:
            lib = get_library(block.library)
            self.parser.add_library(lib)
        except InvalidTemplateLibrary as e:
            raise TemplateSyntaxError(
                "'%s' is not a valid tag library: %s" % (taglib, e)
            )

    def render(self, context):
        try:
            block_name = self.module_name.resolve(context)
            block = modules.get_block(block_name)
        except BlockDoesNotExist:
            return ''
        except template.VariableDoesNotExist:
            return ''

        kwargs = ' '.join(
            '{!s}={!s}'.format(key, val) for key, val in block.kwargs.items()
        )
        tpl = template.Template(
            '{{% load {library} %}}{{% {tag} {kwargs} %}}'.format(
                library=block.library,
                tag=block.tag,
                kwargs=kwargs,
            )
        )
        return tpl.render(context)


@register.tag
def render_module(parser, token):
    bits = token.contents.split()
    module_name = bits[1]
    return RenderModuleNode(parser, module_name)
