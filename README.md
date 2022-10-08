# Heart
This is the web deployment of the heart-disease- prediction. I have used flask to deploy the model.
The link of deployment is:
https://mlheart-disease-prediction-api.herokuapp.com/

## About
The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD).The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.
Variables
Each attribute is a potential risk factor. There are both demographic, behavioral and medical risk factors.</p>

### Demographic:
<li>Sex: male or female(Nominal)</li>
<li> Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
Behavioral</li>
<li>Current Smoker: whether or not the patient is a current smoker (Nominal)</li>
<li> Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)</li>


### Medical( history)
<li> BP Meds: whether or not the patient was on blood pressure medication (Nominal)</li>
<li> Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)</li>
<li> Prevalent Hyp: whether or not the patient was hypertensive (Nominal)</li>
<li> Diabetes: whether or not the patient had diabetes (Nominal)</li>


### Medical(current)
<li> Tot Chol: total cholesterol level (Continuous)</li>
<li> Sys BP: systolic blood pressure (Continuous)</li>
<li> Dia BP: diastolic blood pressure (Continuous)</li>
<li> BMI: Body Mass Index (Continuous)</li>
<li> Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)</li>
<li> Glucose: glucose level (Continuous)</li>


### Predict variable (desired target)
<li>10 year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”)</li>

### Dataset link
"https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression" 
