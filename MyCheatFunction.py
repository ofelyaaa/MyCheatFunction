import numpy as np
import pandas as pd

def cheat(question_number):
  if question_number == "Q1.2P.6":
    sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
    print(np.nvar(sample_scores))
  if question_number == "Q1.2P.7":
    myarray = np.full([4,3,5],np.nan)
    print(myarray)