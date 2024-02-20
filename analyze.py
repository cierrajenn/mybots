import matplotlib.pyplot as plot
import numpy as np

backLegSensorValues = np.load('data/backLegSensorVals.npy')
frontLegSensorValues = np.load('data/frontLegSensorVals.npy')
motorValues = np.load('data/motorVals.npy')
sclMotorValues = np.load('data/scaledMotorVals.npy')
newVals = np.load('data/newMotorVals.npy')

#plot.plot(newVals, np.sin(newVals))
#plot.show()

plot.plot(backLegSensorValues, linewidth = 2, label = 'backLegSensorValues')
plot.plot(frontLegSensorValues, linewidth = 2, label = 'frontLegSensorValues')
plot.legend()
plot.show()

#print(backLegSensorValues)
