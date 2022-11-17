import pandas as pd
from sklearn.tree import DecisionTreeClassifier


Music_data=pd.read_excel('DS1.xlsx')

# Learning with the Model 

X=Music_data.drop (columns=['S/N','DISTRICT NAME', 'ARTIST '])
y=Music_data['ARTIST ']
model= DecisionTreeClassifier()
model.fit(X.values, y)

# Predictions with the model 
predictions = model.predict([[20,1,21]])

print (predictions)



