import matplotlib.pyplot as plt





def EstRTTfun(sample_list,ax):
    outputt=[]
    

    for SampleRTT in sample_list:

        if sample_list[0]==SampleRTT:
            EstimatedRTT = (1- ax)*SampleRTT + ax* SampleRTT

        else:
            EstimatedRTT = (1- ax)* EstimatedRTT+ ax* SampleRTT

        outputt.append(EstimatedRTT)
        

    return outputt
        
        

    


    

#0.000034000 , 0.000034000 , 0.000044000 , 0.000039000 , 0.000032000
#0.000023000 , 0.000017000 , 0.000015000 , 0.000014000 , 0.000053000
#0.000011000 , 0.000011000 , 0.000029000 , 0.000032000 , 0.000017000
#0.000017000 , 0.000025000 , 0.000011000 , 0.000020000 , 0.000022000  
sample=[0.000034000 , 0.000034000 , 0.000044000 , 0.000039000 , 0.000032000,0.000023000 , 0.000017000 , 0.000015000 , 0.000014000 , 0.000053000,0.000011000 , 0.000011000 , 0.000029000 , 0.000032000 , 0.000017000, 0.000017000 , 0.000025000 , 0.000011000 , 0.000020000 , 0.000022000]
a15=EstRTTfun(sample,0.15)
a30=EstRTTfun(sample,0.30)
a45=EstRTTfun(sample,0.45)
a50=EstRTTfun(sample,0.50)
a70=EstRTTfun(sample,0.70)
print(a15)
print("---------------------------------------------------")
print(a30)
print("---------------------------------------------------")
print(a45)
print("---------------------------------------------------")
print(a50)
print("---------------------------------------------------")
print(a70)
line1, =plt.plot(a15,label='alpha=0.15')
plt.legend()
line2, =plt.plot(a30,label='alpha=0.30')
plt.legend()
line3, =plt.plot(a45,label='alpha=0.45')
plt.legend()
line4, =plt.plot(a50,label='alpha=0.50')
plt.legend()
line5, =plt.plot(a70,label='alpha=0.70')
plt.legend()
plt.xlabel('Time (seconds)')
plt.ylabel('RTT (milliseconds')
plt.show()
