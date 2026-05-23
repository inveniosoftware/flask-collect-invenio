# SPDX-FileCopyrightText: 2012 , 2013 Kirill Klenov.
# SPDX-FileCopyrightText: 2014 CERN.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: BSD-3-Clause

"""List files from all static folders."""

from .base import BaseStorage


class Storage(BaseStorage):
    """Dummy storage engine."""

    def run(self):
        """List all file paths."""
        return [f for f in self]
