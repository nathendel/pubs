import sys
import os
import pandas as pd
import numpy

data=pd.read_table("peptides.txt")

intensity_data=data[['Sequence', 'Intensity Control_WCL', 'Intensity Control_WCLP', 'Intensity Onion_rapamycin_WCL', 'Intensity Onion_rapamycin_WCLP']]
control=intensity_data['Intensity Control_WCL'].tolist()
control_P=intensity_data['Intensity Control_WCLP'].tolist()
rap=intensity_data['Intensity Onion_rapamycin_WCL'].tolist()
rap_P=intensity_data['Intensity Onion_rapamycin_WCLP'].tolist()

sum_control=float(numpy.sum(control))
sum_control_P=float(numpy.sum(control_P))
sum_rap=float(numpy.sum(rap))
sum_rap_P=float(numpy.sum(rap_P))

norm_control=[]
norm_control_P=[]
norm_rap=[]
norm_rap_P=[]

for i in range(len(control)):
    if control[i]==0:
        norm_control.append(float(numpy.log2(1/sum_control)))
    else:
        norm_control.append(float(numpy.log2(control[i]/sum_control)))

    if control_P[i]==0:
        norm_control_P.append(float(numpy.log2(1/sum_control_P)))
    else:
        norm_control_P.append(float(numpy.log2(control_P[i]/sum_control_P)))

    if rap[i]==0:
        norm_rap.append(float(numpy.log2(1/sum_rap)))
    else:
        norm_control.append(float(numpy.log2(rap[i]/sum_rap)))

    if rap_P[i]==0:
        norm_rap_P.append(float(numpy.log2(1/sum_control)))
    else:
        norm_rap_P.append(float(numpy.log2(rap_P[i]/sum_control)))


#intensity_data.to_csv('intensity_data.csv')
#read_intensity=open('intensity_data.csv', 'r')

#with open('intensity_data.csv') as f:
#    seq = [str(line.split(",")[0]) for line in f]

#with open('intensity_data.csv') as f:
#    control = [str(line.split(",")[1]) for line in f]

#with open('intensity_data.csv') as f:
#    control = [str(line.split(",")[2]) for line in f]

#with open('intensity_data.csv') as f:
#    control = [str(line.split(",")[3]) for line in f]

#with open('intensity_data.csv') as f:
#    control = [str(line.split(",")[4]) for line in f]

