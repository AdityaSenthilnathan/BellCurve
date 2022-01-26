import random
import plotly_express as py
import plotly.figure_factory as ff
import csv
import pandas as px
"""allVal = []
attempts = []
for i in range(1, 100):      
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceTotal = dice1 + dice2
    allVal.append(diceTotal)
    attempts.append(i)
    """
dataFrame = px.read_csv("StudentData.csv")
figure = ff.create_distplot([dataFrame["Weight(Pounds)"].tolist()], ["Height"])
#figure = ff.create_distplot([allVal], ["attempts"])
figure.show()
