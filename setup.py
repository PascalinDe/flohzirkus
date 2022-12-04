#    Flohzirkus v1.0
#    Copyright (C) 2022  Carine Dengler
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
:synopsis: Package setup.
"""


# standard library imports
# third party imports
from setuptools import setup

# library specific imports
from flohzirkus import METADATA


setup(
    **METADATA,
    packages=["flohzirkus"],
    entry_points={
        "console_scripts": [f"{METADATA['name']}=flohzirkus.__main__:main"]
    },
    install_requires=[
        "python-gitlab",
        "matplotlib",
        "networkx"
    ]

)
