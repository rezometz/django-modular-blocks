[![Build Status](https://travis-ci.org/rezometz/django-modular-blocks.svg?branch=master)](https://travis-ci.org/rezometz/django-modular-blocks)
[![Code Climate](https://codeclimate.com/github/rezometz/django-modular-blocks/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-modular-blocks)
[![Coverage Status](https://coveralls.io/repos/rezometz/django-modular-blocks/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-modular-blocks?branch=master)
# Django Modular Blocks

This app aims at providing a complete set of tools to ease
the deployment of extern applications into a new one.

## Requirements

The only requirements is Django.

## Installation
### Download
Using pip:

    pip install git+ssh://git@github.com/gpichot/django-modular-blocks.git

### Configuring your project
In your settings.py file just add 'modular' to the installed apps:

    INSTALLED_APPS = {
        # ...
        'modular_blocks',
    }

Then, you want the module manager to discover the available modules so
complete your main urls.py file with:

    from modular_blocks import modules
    modules.autodiscover()
    
    urlpatterns = patterns('',
        # your patterns
    )

    urlpatterns += modules.get_patterns()

If you use `i18n_patterns` :

    urlpatterns += modules.get_i18n_patterns()

Then, load any module that you want from a template using the render module
tag from the modules tag library. In the following example we are using the 
TwoModularColumnsMixin class to add two attributes (left and right sidebars)
to our user object (and using AUTH_USER_MODEL variable).

    {% load modules %}
    {% for module in request.user.sidebar_left %}
        <div class="module">
            {% render_module module %}
        </div>
    {% endfor %}
