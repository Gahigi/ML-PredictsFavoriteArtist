import pandas as pd
from sklearn import svm
import joblib


Music_data=pd.read_excel('DS1.xlsx')

# Learning with the Model 

X=Music_data.drop (columns=['S/N','DISTRICT NAME', 'ARTIST '])
y=Music_data['ARTIST ']
model= svm.SVC(kernel='linear')
model.fit(X.values, y)

# Create a persistent Model

joblib.dump(model, 'music-recommender.joblib')
