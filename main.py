# I want to build a Minecraft building classifier
# I will use a Neural Network to do this
# Pytorch is the library I will use to build the Neural Network
# I will use the nbtschematic library to read the Minecraft building schematics

# Import libraries
import numpy as np
from nbtschematic import SchematicFile
import numpy as np
import matplotlib.pyplot as plt


sf = SchematicFile.load("schematics/apple.schematic")


print(np.asarray(sf.blocks))
