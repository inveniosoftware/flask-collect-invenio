# SPDX-FileCopyrightText: 2012 , 2014 Kirill Klenov.
# SPDX-FileCopyrightText: 2014 , 2016 CERN.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: BSD-3-Clause

"""Copy files from all static folders to root folder."""

from os import makedirs
from os import path as op
from os import remove
from shutil import copy

from .base import BaseStorage


class Storage(BaseStorage):
    """Storage that copies static files."""

    def run(self):
        """Collect static files from blueprints."""
        self.log("Collect static from blueprints.")

        for bp, f, o in self:
            destination = op.join(self.collect.static_root, o)

            destination_dir = op.dirname(destination)
            if not op.exists(destination_dir):
                makedirs(destination_dir)

            if op.exists(destination):

                if op.getmtime(destination) >= op.getmtime(f):
                    continue

                remove(destination)

            copy(f, destination)
            self.log(
                "Copied: [{0}] '{1}'".format(
                    bp.name, op.join(self.collect.static_url, destination)
                )
            )
