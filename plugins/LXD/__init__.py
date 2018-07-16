# Copyright (c) 2014,2018 ADLINK Technology Inc.
# 
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
# 
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0
# 
# SPDX-License-Identifier: EPL-2.0
#
# Contributors: Gabriele Baldoni, ADLINK Technology Inc. - Base plugins set

import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(file_dir))

VERSION = 1


def run(*args, **kwargs):
    sys.path.append(os.path.join(sys.path[0], 'plugins', 'LXD'))
    from LXD_plugin import LXD
    lxd = LXD('LXD', VERSION, kwargs.get('agent'), kwargs.get('uuid'))
    return lxd

