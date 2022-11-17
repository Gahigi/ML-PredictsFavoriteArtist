import pandas as pd
from sklearn import svm
import joblib
model=joblib.load('music-recommender.joblib')
Age=int (input ("Enter Age :"))
Gender= input ("Enter Gender (1 for Male and 0 for Female): ")
Dis=int (input ("Enter District Number :"))

predictions = model.predict ([[Age,Gender,Dis]])
print("The Artist you like is:",predictions )

        
                                        






