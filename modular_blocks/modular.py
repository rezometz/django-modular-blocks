from django.conf.urls import include, url

from modular_blocks import ModuleApp, modules

from . import urls


class ModularModule(ModuleApp):
    app_name = 'modular_blocks'
    name = 'modular'
    urls = url('^modular/', include(urls))
modules.register(ModularModule)
