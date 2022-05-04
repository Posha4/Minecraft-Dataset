import anvil

def layerdisplay(layer):
    for i in layer :
        print(i)

region = anvil.Region.from_file('Main/r.0.0.mca')

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global

ch = range(0,16)
scan_height = 100

layers = []
layer = []
line = []

for j in range(scan_height) :
    print("Layer", j)

    for i in ch :

        line = []
        for k in ch :
            block = chunk.get_block(i,j,k)
            line.append(block.id[0:3])
        layer.append(line)        

    layers.append(layer)

    layerdisplay(layer)

    layer = []


#print(block) # <Block(minecraft:air)>
#print(block.id) # air
#print(block.properties) # {}

