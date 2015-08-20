import os

import logging

from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls.i18n import i18n_patterns


logger = logging.getLogger(__name__)


class ModuleDoesNotExist(Exception):
    pass


class BlockDoesNotExist(Exception):
    pass


class ModuleApp(object):
    templatetag_blocks = []

    def get_name(self):
        try:
            return self.name
        except:
            print 'You app have to provide a name'

    def get_blocks(self):
        return self.templatetag_blocks


class TemplateTagBlock(object):
    name = None
    module = None

    def __init__(self, name=None, cache_time=None, library=None, tag=None,
                 kwargs={}):
        self.name = name
        self.cache_time = cache_time
        self.library = library
        self.tag = tag
        self.kwargs = kwargs

    def title(self):
        try:
            return self.block_title
        except AttributeError:
            return self.name.capitalize()

    def get_tag(self):
        path = self.get_relative_tag_path().split('.')
        module = __import__(self.get_full_path())
        for submodule in path:
            module = getattr(module, submodule)

        return module

    def get_relative_tag_path(self):
        return 'templatetags.{library}.{tag}'.format(
            library=self.library,
            tag=self.tag,
        )

    def get_full_path(self):
        return '{app_name}.templatetags.{library}'.format(
            app_name=self.module.app_name,
            library=self.library,
        )


class ModuleLibrary(object):
    modules = {}
    blocks = {}
    urls = []

    def register(self, module_class):
        self.modules[module_class.name] = module_class()
        for block in module_class.templatetag_blocks:
            block.module = module_class
            self.blocks[block.name] = block
        if module_class.urls is not None:
            self.urls.append(module_class.urls)

    def get_block(self, name):
        try:
            return self.blocks[name]
        except KeyError:
            logger.error(
                'The module manager failed to load the block {name}.'
                'Is it registered ?'.format(name=name)
            )
            raise BlockDoesNotExist(name)

    def get(self, module_name):
        try:
            return self.modules[module_name]
        except KeyError:
            raise ModuleDoesNotExist(
                'The module manager failed to load the module {module_name}.'
                'Is it registered ?'.format(module_name=module_name)
            )

    def get_non_used_blocks(self, *names):
        return [
            block for name, block in self.blocks.items()
            if name not in names
        ]

    def all(self):
        return self.modules

    def get_patterns(self):
        return patterns('', *self.urls)

    def get_i18n_patterns(self):
        return i18n_patterns('', *self.urls)

    def autodiscover(self):
        for app in settings.INSTALLED_APPS:
            try:
                __import__(app + '.modular')
            except ImportError:
                pass


modules = ModuleLibrary()
