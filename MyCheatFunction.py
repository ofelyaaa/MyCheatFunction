import numpy as np
import pandas as pd

def cheat(question_number):
  if question_number == "Q1.2P.9":
    np.random.seed(1234)  # Set the random seed
    speed_sec = np.zeros(10)
    sim_speed = np.random.uniform(size=5)  # Speed simulation in seconds
    speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5)
    speed_sec[5:10] = sim_speed

    d = {'language': list(['R'] * 5 + ['Python'] * 5),
         'codetype': list([f'forloop{i}' for i in range(1, 6)] * 2),
         'speed': speed_sec}
    simmydf = pd.DataFrame.from_dict(d)
    print(simmydf)
  if question_number == "Q1.2P.7":
    myarray = np.full([4,3,5],np.nan)
    print(myarray)
