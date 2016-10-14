#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages
import os



# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# TEMPLATES = [
#     {
#         "DIRS": [
#             os.path.join(BASE_DIR, "templates/emails/"),
#         ],
#     }
# ]

setup(
    name = "taiga-contrib-email-overrides",
    version = ":versiontools:taiga_contrib_email_overrides:",
    description = "The Taiga plugin for custom templates",
    long_description = "",
    keywords = 'taiga, Email, integration',
    author = 'Studiofonkel',
    author_email = 'info@studiofonkel.nl',
    url = 'https://github.com/studio-fonkel/taiga-email-overrides',
    license = '',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        'Programming Language :: Python',
    ],
)
