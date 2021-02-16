################################################## DOBRE###############################################################
from docplex.mp.model import Model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
#import gurobipy as gp
import regex as re

Y = {(i,j) for i in range(15) for j in range(18)}
X = {(0,j) for j in range(18)}

print('##################################')
print(len(Y))
print(len(X))
print('##################################')


dystanse = pd.read_excel('domatlaba2.xlsx')
print(dystanse)

dane = ''

liczbalotnisk=15
p = [i for i in range(1, liczbalotnisk+1)]
print(p)


for o in range(0, len(p)):
    Modelowe = Model('Pcenter')
    x = Modelowe.binary_var_dict(X,name='x')
    y = Modelowe.binary_var_dict(Y,name='y')
    
    r = Modelowe.continuous_var(name='r')
    print('##################################')
    print(p[o])
    print('##################################')
    Modelowe.add_constraints(Modelowe.sum(dystanse.iloc[i,j]*y[i,j] for i in range (15))<=r for j in range(18))
    Modelowe.add_constraints(Modelowe.sum(y[i,j] for i in range (15))==1 for j in range(18))

    #print(Model.sum(x[i] for i in range(18)))
    Modelowe.add_constraint(Modelowe.sum(x[0,i] for i in range(18))==p[o])

    #Model.add_constraints(Model.sum(y[i,j] for i in range(15))-x[j] <=0 for j in range (17))
    for i in range(15):
        for j in range(18):
            Modelowe.add_constraint(y[i,j]-x[0,i] <=0)

    #Model.add_constraints(Model.sum(list(x.values()))==p)

    Modelowe.minimize(r)
    rozwiązanie = Modelowe.solve(log_output = True)
    print(rozwiązanie)
    
    for index, dvar in enumerate(rozwiązanie.iter_variables()):
        dane = dane+','+dvar.to_string()


d = {}

for x in range(0, 18):
    for q in range(0,15):
        c = "y_"+str(q)+"_"+str(x)
        test = r"\b"+str(c)+"\\"+"b" 
        #print(test)
        print(c)
        #b = dane.count(c)
        b = sum(1 for match in re.finditer(r"\b"+str(c)+"\\"+"b", dane))
        print(b)
        d["centrum{}_{}".format(q,x)] = b
        

keys, values = zip(*d.items()) 

print ("keys : ", str(keys)) 
print ("values : ", str(values))        
        
print(d)
print(len(d))
print(sum(values))
valuesy=list(d.values())


output=[]
wiersze=18
kolumny=15

for i in range(wiersze):
  output.append([])
  for j in range(kolumny):
     output[i].append(valuesy[i*kolumny+j])
print(output)

wynikowe = [sum(x) for x in zip(*output)]
print('############################################### WYNIKI #########################################################')
print(wynikowe)
print('################################################################################################################')
sumawszystkiego = sum(wynikowe)
print(sumawszystkiego)
#print(values)
#print(valuesy)

