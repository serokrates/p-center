################################################## DOBRE###############################################################
from itertools import product
from math import sqrt
import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import numpy as np

dystanse = pd.read_excel('domatlaba2.xlsx')
liczbalotnisk = 15
wynik = np.zeros((15, 18))
N = [i for i in range(1, liczbalotnisk+1)]
print(N)

#print(N[d])
for d in range(0, len(N)):
    print(N[d])
    m = gp.Model('pcenter')

    r = m.addMVar(1)
    x = m.addMVar((1,18), vtype=GRB.BINARY)
    y = m.addMVar((15,18), vtype=GRB.BINARY)
    print(r)
    print(x)
    print(y)


    m.addConstrs(sum(dystanse.iloc[i,j]*y[i,j] for i in range (15))<=r for j in range(18))
    m.addConstrs(sum(y[i,j] for i in range(15))==1 for j in range(18))

    #print(Model.sum(x[i] for i in range(18)))
    #m.addConstr(sum(x[0,i] for i in range(18))<=18)
    #m.addConstr(sum(y[i,j] for i in range(15) for j in range(18))==N[d])
    
    m.addConstr(sum(x[0,i] for i in range(18))==N[d])
    #m.addConstr(sum(y[i,j] for i in range(15) for j in range(18))==18)

    #Model.add_constraints(Model.sum(y[i,j] for i in range(15))-x[j] <=0 for j in range (18))
    for i in range(15):
        for j in range(18):
            m.addConstr(y[i,j]-x[0,i] <=0)

    m.setObjective(r, GRB.MINIMIZE)
    ################################################################################################################


    m.optimize()
    print('################################################################################################################')
    #t = x.keys()
    #tt = y.keys()
    print(x.X)
    print(y.X)
    wynik = wynik + y.X
    #print(tt)
    print('################################################################################################################')
print(wynik)
wynik2 = sum(sum(wynik))
print(wynik2)
wynik3 = np.sum(wynik, axis = 1)
print('############################################### WYNIKI #########################################################')
print(wynik3)
print('################################################################################################################')
