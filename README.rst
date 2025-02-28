==============
City Locations
==============

City Locations is a Django app that can be installed in an existing Django project
Documentation: https://toddpy-django-cityloc-pkg.readthedocs.io/en/latest/

Installation
------------

1. Add "citylocations" to your INSTALLED_APPS setting in settings.py:
    INSTALLED_APPS = [
        ...
        'citylocations',
    ]

2. Include the citylocations URLconf in your project urls.py like this::

    path('', include('citylocations.urls')),

3. Start the development server and visit http://127.0.0.1:8000/
In the django_cityloc_pkg/ folder, create a file named setup.cfg and add the content below.
The setup.cfg file defines the parameters that are used to build your package. These parameters are also used by installation tools to verify dependencies, and used to document supported usages in PyPI.

setup.cfg content:

[metadata]
    name = django_cityloc_pkg_hm-pfeiffer
    version = 0.0.1
    description = A Django app about city locations
    author = Author Name
    author_email = authoremail@example.com
    classifiers =
        Environment :: Web Environment
        Framework :: Django
        Framework :: Django :: 3.2
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 3.9    
    
    [options]
    include_package_data = true
    packages = find:
    python_requires = >=3.8
    install_requires =
        Django >= 3.2
            