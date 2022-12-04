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
:synopsis: Command-line interface.
"""


# standard library imports
import re
import argparse

# third party imports
from flohzirkus import METADATA

# library specific imports


VALID_CHARS = r"[-._0-9A-Za-z]+"


def _project_id(project_id):
    """Assert project ID is a valid project ID.

    :param str project_id: project ID

    :returns: project_id
    :rtype: str
    """
    if re.fullmatch(r"[0-9]+", project_id):
        return project_id
    if re.fullmatch(rf"{VALID_CHARS}/{VALID_CHARS}", project_id):
        return project_id
    raise argparse.ArgumentTypeError(
        f"'{project_id}' is not a valid project ID"
    )


def _parameters(unknown_args):
    """Parse unknown arguments.

    :param list unknown_args: unknown arguments

    :returns: issues API parameters
    :rtype: dict
    """
    pattern = rf"({VALID_CHARS})=({VALID_CHARS})"
    parameters = {}
    for arg in unknown_args:
        if match := re.fullmatch(pattern, arg):
            value = match.group(2)
            if re.fullmatch(r"[0-9]+", value):
                value = int(value)
            if value.lower() in ("true", "false"):
                value = (value == "true")
            parameters[match.group(1)] = value
        else:
            raise argparse.ArgumentTypeError(
                f"'{arg}' is not a valid issues API parameter"
            )
    return parameters


def init_argument_parser():
    """Initialize argument parser.

    :returns: argument parser
    :rtype: ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog=METADATA["name"],
        description=METADATA["description"],
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--url",
        default="https://gitlab.com/",
        help="GitLab server URL"
    )
    parser.add_argument(
        "--private_token",
        help="private token"
    )
    parser.add_argument(
        "--http_username",
        help="HTTP authentication username"
    )
    parser.add_argument(
        "--http_password",
        help="HTTP authentication password"
    )
    parser.add_argument(
        "--dump",
        action="store_true",
        help="toggle dumping graph on/off"
    )
    parser.add_argument(
        "--draw",
        action="store_true",
        help="toggle drawing graph on/off"
    )
    parser.add_argument(
        "project_id",
        type=_project_id,
        help="project ID"
    )
    return parser
