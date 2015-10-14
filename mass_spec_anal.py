import sys
import os
import pandas as pd
import numpy
import matplotlib.pyplot as plt


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
        norm_rap.append(float(numpy.log2(rap[i]/sum_rap)))

    if rap_P[i]==0:
        norm_rap_P.append(float(numpy.log2(1/sum_rap_P)))
    else:
        norm_rap_P.append(float(numpy.log2(rap_P[i]/sum_rap_P)))


#for i in len(I_control):
#    print I_control(i)

# plt.hist(intensities, 3)
# plt.show()

def subList(list1,list2):
    return [x-y for x,y in zip(list1,list2)]

diffRapControl = subList(norm_rap,norm_control)
diffControlPhos_Control = subList(norm_control_P,norm_control)
diffRapPhos_Rap = subList(norm_rap,norm_rap_P)
diffrapPhos_ControlPhos = subList(norm_rap_P, norm_control_P)

plt.hist(diffRapControl,100)
plt.title('difference between rap and control')
plt.ylim(0, 2000)
plt.show()

plt.hist(diffControlPhos_Control,100)
plt.title('difference between control(Phos) and control')
plt.ylim(0, 2000)
plt.show()

plt.hist(diffRapPhos_Rap,100)
plt.title('difference between rap and rap(phos)')
plt.ylim(0, 2000)
plt.show()

# plt.hist(diffrapPhos_ControlPhos,100)
# plt.title('difference between rap(phos) and control(phos)')
# plt.ylim(0, 600)
# plt.show()



