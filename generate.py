import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

# original box position
x = 0
y = 0
z = 0.5

# columns 
for _ in range(5):
    # reset x for start of new row
    x = 0
    
    # rows
    for _ in range(5):
        # reset z for start of new tower
        z = 0.5
        # original box dimensions
        length = 1
        height = 1
        width = 1

        # creates each tower of 10
        for _ in range(10):
            pyrosim.Send_Cube(name = "Box", pos = [x, y, z], size = [length, width, height])
            # update cube dimensions
            length *= .9
            height *= .9
            width *= .9
            z += 1
        x += 1
    y += 1
    

pyrosim.End()
