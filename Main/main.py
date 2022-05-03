import mcworldlib as mc

import os
cwd = os.getcwd()
print(cwd)
world = mc.load('world')
# Most classes have a pretty print. In many cases, their NBT data.
mc.pretty(world.level)
