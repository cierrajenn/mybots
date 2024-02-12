import matplotlib.pyplot as plot
import numpy as np

backLegSensorValues = np.load('data/backLegSensorVals.npy')
frontLegSensorValues = np.load('data/frontLegSensorVals.npy')

plot.plot(backLegSensorValues, linewidth = 2, label = 'backLegSensorValues')
plot.plot(frontLegSensorValues, linewidth = 2, label = 'frontLegSensorValues')
plot.legend()
plot.show()

#print(backLegSensorValues)
