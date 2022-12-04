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
:synopsis: GitLab utils.
"""


# standard library imports

# third party imports

# library specific imports


def get_links(issue, **parameters):
    """Get links.

    :param Issue issue: issue
    :param dict parameters: issue links API parameters

    :returns: links
    :rtype: generator
    """
    return issue.links.list(iterator=True, **parameters)


def get_issues(client, project_id, **parameters):
    """Get issues.

    :param Gitlab client: client
    :param str project_id: project ID
    :param dict parameters: issues API parameters

    :returns: issues
    :rtype: generator
    """
    project = client.projects.get(project_id)
    return project.issues.list(iterator=True, **parameters)
