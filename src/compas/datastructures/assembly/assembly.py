from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.datastructures import Network


__author__    = ['Tom Van Mele', ]
__copyright__ = 'Copyright 2016 - Block Research Group, ETH Zurich'
__license__   = 'MIT License'
__email__     = 'vanmelet@ethz.ch'


__all__ = ['Assembly', ]


class Assembly(Network):
    """"""

    def __init__(self):
        super(Assembly, self).__init__()
        self.blocks = {}
        self.default_vertex_attributes.update({
            'is_support': False
        })
        self.default_edge_attributes.update({
            'interface_points' : None,
            'interface_type'   : None,
            'interface_size'   : None,
            'interface_uvw'    : None,
            'interface_origin' : None,
            'interface_forces' : None,
        })

    def add_block(self, block, attr_dict=None, **kwattr):
        x, y, z = block.centroid()
        key = self.add_vertex(attr_dict=attr_dict, x=x, y=y, z=z, **kwattr)
        self.blocks[key] = block

    def add_support(self, block, attr_dict=None, **kwattr):
        x, y, z = block.centroid()
        key = self.add_vertex(attr_dict=attr_dict, x=x, y=y, z=z, is_support=True, **kwattr)
        self.blocks[key] = block

    def add_interface(self):
        pass

    def identify_interfaces(self):
        pass


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
