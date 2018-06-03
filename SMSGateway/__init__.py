# -*- coding: utf-8 -*-
#
# This file is part of the SMSGateway project
#
#
#
# Distributed under the terms of the MIT license.
# See LICENSE.txt for more info.

"""SMSGateway for PANIC

"""

from . import release
from .SMSGateway import SMSGateway, main

__version__ = release.version
__version_info__ = release.version_info
__author__ = release.author
