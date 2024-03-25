from hillclimber import HILL_CLIMBER

import os

hc = HILL_CLIMBER()

hc.evolve()
hc.show_best()

##for i in range(5):
##    os.system("python3 generate.py")
##    os.system("python3 simulate.py")
