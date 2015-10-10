from django import template
from django.template.base import (
    Node,
    InvalidTemplateLibrary,
    get_library,
)

from .. import modules, BlockDoesNotExist


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
            raise template.TemplateSyntaxError(
                "'%s' is not a valid tag library: %s" % (block.library, e)
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
        if block.cache_time > 0:
            if block.personal:
                string = '{{% load cache %}}{{% load {library} %}}\
                    {{% cache {cache_time} {slug} request.user.username %}}\
                    {{% {tag} {kwargs} %}}{{% endcache %}}'
            else:
                string = '{{% load cache %}}{{% load {library} %}}\
                    {{% cache {cache_time} {slug} %}}\
                    {{% {tag} {kwargs} %}}{{% endcache %}}'
            tpl = template.Template(string.format(
                    library=block.library,
                    cache_time=block.cache_time,
                    slug=block.tag,
                    tag=block.tag,
                    kwargs=kwargs,
                )
            )
        else:
            string = '{{% load {library} %}}{{% {tag} {kwargs} %}}'
            tpl = template.Template(string.format(
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
