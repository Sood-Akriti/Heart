
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
heart_df=pd.read_csv("C:/Users/Anchal/Desktop/heart_disease/framingham.csv")
## Replacing null values with the mean value
heart_df["education"].fillna(heart_df["education"].mean(),inplace=True)
heart_df["cigsPerDay"].fillna(heart_df["cigsPerDay"].mean(),inplace=True)
heart_df["BPMeds"].fillna(heart_df["BPMeds"].mean(),inplace=True)
heart_df["totChol"].fillna(heart_df["totChol"].mean(),inplace=True)
heart_df["BMI"].fillna(heart_df["BMI"].mean(),inplace=True)
heart_df["heartRate"].fillna(heart_df["heartRate"].mean(),inplace=True)
heart_df["glucose"].fillna(heart_df["glucose"].mean(),inplace=True)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
## Defining variables X,y 
X= heart_df.drop("TenYearCHD",axis=1)
y=heart_df["TenYearCHD"]
print("Columns in X :",X.columns)
print("y :",y)
print("shape of X:",X.shape)
print("shape of y:",y.shape[0])

col_names = heart_df.columns
 
for c in col_names:
    heart_df = heart_df.replace("?", np.NaN)
heart_df = heart_df.apply(lambda x: x.fillna(x.value_counts().index[0]))

category_col=[i for i in heart_df.columns if heart_df[i].dtypes=='object']
from sklearn.preprocessing import LabelEncoder
labelEncoder=LabelEncoder()
mapping_dict = {}
for col in category_col:
    heart_df[col] = labelEncoder.fit_transform(heart_df[col])
 
    le_name_mapping = dict(zip(labelEncoder.classes_,
                               labelEncoder.transform(labelEncoder.classes_)))
 
    mapping_dict[col] = le_name_mapping
print(mapping_dict)
    
## Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
## Scaling the data 
sc= StandardScaler()
X_train = sc.fit_transform(X_train)
X_test=sc.transform(X_test)
X_train=pd.DataFrame(X_train,columns=X.columns)
X_test=pd.DataFrame(X_test,columns=X.columns)
## Training the model using Logistic Regression
regressor=LogisticRegression()
regressor.fit(X_train,y_train)
import pickle
file_name='heart_prediction.pkl'
f = open(file_name,'wb')
pickle. dump(regressor,f)
f. close()
heart_prediction = pickle.load(open('heart_prediction.pkl','rb'))