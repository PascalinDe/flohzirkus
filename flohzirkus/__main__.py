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
:synopsis: Main routine.
"""


# standard library imports
import logging

# third party imports
import gitlab

# library specific imports
import flohzirkus.cli
import flohzirkus.graph
import flohzirkus.gitlab


def main():
    """Main routine."""
    logging.basicConfig(
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
        level=logging.INFO
    )
    args, unknown_args = flohzirkus.cli.init_argument_parser().parse_known_args()   # noqa
    parameters = flohzirkus.cli._parameters(unknown_args)
    client = gitlab.Gitlab(
        **{
            key: getattr(args, key)
            for key in (
                "url",
                "private_token",
                "http_username",
                "http_password"
            )
        }
    )
    issues = flohzirkus.gitlab.get_issues(
        client,
        args.project_id,
        **parameters
    )
    edge_list = []
    for issue in issues:
        edge_list += [
            (issue.references["full"], link.references["full"])
            for link in flohzirkus.gitlab.get_links(
                issue,
                link_type="relates_to"
            )
        ]
    flohzirkus.graph.handle_graph(edge_list, dump=args.dump, draw=args.draw)


if __name__ == "__main__":
    main()
