#!/usr/bin/env sh
# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2021 TU Wien.
# SPDX-License-Identifier: BSD-3-Clause

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

black --check --diff flask_collect tests
sphinx-build -qnN docs docs/_build/html
pytest
