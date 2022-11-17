import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


Music_data=pd.read_excel('DS1.xlsx')

# Split dataset into training set and test set

X=Music_data.drop (columns=['S/N','DISTRICT NAME', 'ARTIST '])
y=Music_data['ARTIST ']
X_train, x_test, y_train, y_test=train_test_split (X,y, test_size=0.2)

#Create a Decision Tree, Logistic Regression, Suport Vector Machine  and Random Forest Classifiers

Decision_tree_model= DecisionTreeClassifier()
Logistic_regression_Model=LogisticRegression(solver='lbfgs',max_iter=10000)
SVM_model=svm.SVC(kernel='linear')
RF_model=RandomForestClassifier(n_estimators=100)

#Train the models using the training sets

Decision_tree_model.fit(X_train, y_train)
Logistic_regression_Model.fit(X_train, y_train)
SVM_model.fit(X_train, y_train)
RF_model.fit(X_train, y_train)

#Predict the response for test dataset

DT_Prediction =Decision_tree_model.predict(x_test)
LR_Prediction =Logistic_regression_Model.predict(x_test)
SVM_Prediction =SVM_model.predict(x_test)
RF_Prediction =RF_model.predict(x_test)

# Calculation of Model Accuracy

DT_score=accuracy_score(y_test, DT_Prediction)
lR_score=accuracy_score(y_test, LR_Prediction)
SVM_score=accuracy_score(y_test, SVM_Prediction)
RF_score=accuracy_score(y_test, RF_Prediction)

# Display Accuracy

print ("Decistion Tree accuracy =", DT_score*100,"%")
print ("Logistic Regression accuracy =", lR_score*100,"%")
print ("Suport Vector Machine accuracy =", SVM_score*100,"%")
print ("Random Forest accuracy =", RF_score*100,"%")

