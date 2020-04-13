#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2015-2018 Cisco Systems, Inc.
#  Copyright (c) 2020 Gonéri Le Bouder
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import contextlib
import datetime
import io
import os
import subprocess
import sys

import molecule
import molecule.config
import molecule.util

try:
    import virt_lightning
except ImportError:
    sys.exit("ERROR: Virt-Lightning missing, install virt-lightning Python module.")
ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = ""

EXAMPLES = ""

RETURN = ""


def main():
    module = AnsibleModule(
        argument_spec=dict(
            instance_name=dict(type="str", required=True),
            instance_interfaces=dict(type="list", default=[]),
            instance_raw_config_args=dict(type="list", default=None),
            config_options=dict(type="dict", default={}),
            platform_box=dict(type="str", required=False),
            platform_box_version=dict(type="str"),
            platform_box_url=dict(type="str"),
            provider_name=dict(type="str", default="virtualbox"),
            provider_memory=dict(type="int", default=512),
            provider_cpus=dict(type="int", default=2),
            provider_options=dict(type="dict", default={}),
            provider_override_args=dict(type="list", default=None),
            provider_raw_config_args=dict(type="list", default=None),
            provision=dict(type="bool", default=False),
            force_stop=dict(type="bool", default=False),
            state=dict(type="str", default="up", choices=["up", "destroy", "halt"]),
        ),
        supports_check_mode=False,
    )

    if module.params["state"] == "up":
        pass

    if module.params["state"] == "destroy":
        pass

    if module.params["state"] == "halt":
        pass

    module.exit_json(**module.result)


if __name__ == "__main__":
    main()
