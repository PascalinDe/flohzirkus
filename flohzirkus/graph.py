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
:synopsis: Graph utils.
"""


# standard library imports
import json
import pathlib
import tempfile

# third party imports
import networkx
import matplotlib.pyplot

# library specific imports
from flohzirkus import METADATA


def handle_graph(edge_list, dump=False, draw=False):
    """Handle graph.

    :param iterable edge_list: edge list
    :param bool dump: toggle dumping graph on/off
    :param bool draw: toggle drawing graph on/off

    :returns: graph
    :rtype: Graph
    """
    graph = networkx.Graph(edge_list)
    if dump:
        with (
            pathlib.Path(tempfile.gettempdir()) / f"{METADATA['name']}.json"
        ).open("w") as fp:
            json.dump(networkx.node_link_data(graph), fp)
    if draw:
        networkx.draw(graph, with_labels=True)
        matplotlib.pyplot.show()
    return graph
