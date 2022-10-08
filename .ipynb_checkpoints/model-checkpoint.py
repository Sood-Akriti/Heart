{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "baf41f72",
   "metadata": {
    "papermill": {
     "duration": 0.077933,
     "end_time": "2022-03-20T16:29:50.522594",
     "exception": false,
     "start_time": "2022-03-20T16:29:50.444661",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **IMPORTING DATA**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "978ed1a0",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:50.718290Z",
     "iopub.status.busy": "2022-03-20T16:29:50.717393Z",
     "iopub.status.idle": "2022-03-20T16:29:51.760959Z",
     "shell.execute_reply": "2022-03-20T16:29:51.760229Z",
     "shell.execute_reply.started": "2022-03-20T15:06:56.778324Z"
    },
    "papermill": {
     "duration": 1.158132,
     "end_time": "2022-03-20T16:29:51.761125",
     "exception": false,
     "start_time": "2022-03-20T16:29:50.602993",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "\n",
    "import os\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e740ab82",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:51.926581Z",
     "iopub.status.busy": "2022-03-20T16:29:51.925889Z",
     "iopub.status.idle": "2022-03-20T16:29:51.951956Z",
     "shell.execute_reply": "2022-03-20T16:29:51.952455Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.326889Z"
    },
    "papermill": {
     "duration": 0.111568,
     "end_time": "2022-03-20T16:29:51.952640",
     "exception": false,
     "start_time": "2022-03-20T16:29:51.841072",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "heart_df=pd.read_csv(\"C:/Users/Anchal/Desktop/heart_disease/framingham.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b5f71e3",
   "metadata": {
    "papermill": {
     "duration": 0.078631,
     "end_time": "2022-03-20T16:29:52.112111",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.033480",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **DATA EXPLORATION**\n",
    "\n",
    "> Data exploration is the initial step in data analysis, where users explore a large data set in an unstructured way to uncover initial patterns, characteristics, and points of interest. This process isn’t meant to reveal every bit of information a dataset holds, but rather to help create a broad picture of important trends and major points to study in greater detai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5ad583cb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:52.271993Z",
     "iopub.status.busy": "2022-03-20T16:29:52.271389Z",
     "iopub.status.idle": "2022-03-20T16:29:52.277568Z",
     "shell.execute_reply": "2022-03-20T16:29:52.278146Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.350716Z"
    },
    "papermill": {
     "duration": 0.087894,
     "end_time": "2022-03-20T16:29:52.278331",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.190437",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4238, 16)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## shape \n",
    "heart_df.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "96e06548",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:52.438809Z",
     "iopub.status.busy": "2022-03-20T16:29:52.438193Z",
     "iopub.status.idle": "2022-03-20T16:29:52.463487Z",
     "shell.execute_reply": "2022-03-20T16:29:52.464064Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.361302Z"
    },
    "papermill": {
     "duration": 0.107215,
     "end_time": "2022-03-20T16:29:52.464256",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.357041",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>male</th>\n",
       "      <th>age</th>\n",
       "      <th>education</th>\n",
       "      <th>currentSmoker</th>\n",
       "      <th>cigsPerDay</th>\n",
       "      <th>BPMeds</th>\n",
       "      <th>prevalentStroke</th>\n",
       "      <th>prevalentHyp</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>totChol</th>\n",
       "      <th>sysBP</th>\n",
       "      <th>diaBP</th>\n",
       "      <th>BMI</th>\n",
       "      <th>heartRate</th>\n",
       "      <th>glucose</th>\n",
       "      <th>TenYearCHD</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>195.0</td>\n",
       "      <td>106.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>26.97</td>\n",
       "      <td>80.0</td>\n",
       "      <td>77.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>46</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>250.0</td>\n",
       "      <td>121.0</td>\n",
       "      <td>81.0</td>\n",
       "      <td>28.73</td>\n",
       "      <td>95.0</td>\n",
       "      <td>76.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>48</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>245.0</td>\n",
       "      <td>127.5</td>\n",
       "      <td>80.0</td>\n",
       "      <td>25.34</td>\n",
       "      <td>75.0</td>\n",
       "      <td>70.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>61</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>30.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>225.0</td>\n",
       "      <td>150.0</td>\n",
       "      <td>95.0</td>\n",
       "      <td>28.58</td>\n",
       "      <td>65.0</td>\n",
       "      <td>103.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>46</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>23.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>285.0</td>\n",
       "      <td>130.0</td>\n",
       "      <td>84.0</td>\n",
       "      <td>23.10</td>\n",
       "      <td>85.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   male  age  education  currentSmoker  cigsPerDay  BPMeds  prevalentStroke  \\\n",
       "0     1   39        4.0              0         0.0     0.0                0   \n",
       "1     0   46        2.0              0         0.0     0.0                0   \n",
       "2     1   48        1.0              1        20.0     0.0                0   \n",
       "3     0   61        3.0              1        30.0     0.0                0   \n",
       "4     0   46        3.0              1        23.0     0.0                0   \n",
       "\n",
       "   prevalentHyp  diabetes  totChol  sysBP  diaBP    BMI  heartRate  glucose  \\\n",
       "0             0         0    195.0  106.0   70.0  26.97       80.0     77.0   \n",
       "1             0         0    250.0  121.0   81.0  28.73       95.0     76.0   \n",
       "2             0         0    245.0  127.5   80.0  25.34       75.0     70.0   \n",
       "3             1         0    225.0  150.0   95.0  28.58       65.0    103.0   \n",
       "4             0         0    285.0  130.0   84.0  23.10       85.0     85.0   \n",
       "\n",
       "   TenYearCHD  \n",
       "0           0  \n",
       "1           0  \n",
       "2           0  \n",
       "3           1  \n",
       "4           0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## 1st five columns\n",
    "heart_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c96a4109",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:52.629617Z",
     "iopub.status.busy": "2022-03-20T16:29:52.626344Z",
     "iopub.status.idle": "2022-03-20T16:29:52.651111Z",
     "shell.execute_reply": "2022-03-20T16:29:52.651677Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.397023Z"
    },
    "papermill": {
     "duration": 0.108499,
     "end_time": "2022-03-20T16:29:52.651854",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.543355",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4238 entries, 0 to 4237\n",
      "Data columns (total 16 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   male             4238 non-null   int64  \n",
      " 1   age              4238 non-null   int64  \n",
      " 2   education        4133 non-null   float64\n",
      " 3   currentSmoker    4238 non-null   int64  \n",
      " 4   cigsPerDay       4209 non-null   float64\n",
      " 5   BPMeds           4185 non-null   float64\n",
      " 6   prevalentStroke  4238 non-null   int64  \n",
      " 7   prevalentHyp     4238 non-null   int64  \n",
      " 8   diabetes         4238 non-null   int64  \n",
      " 9   totChol          4188 non-null   float64\n",
      " 10  sysBP            4238 non-null   float64\n",
      " 11  diaBP            4238 non-null   float64\n",
      " 12  BMI              4219 non-null   float64\n",
      " 13  heartRate        4237 non-null   float64\n",
      " 14  glucose          3850 non-null   float64\n",
      " 15  TenYearCHD       4238 non-null   int64  \n",
      "dtypes: float64(9), int64(7)\n",
      "memory usage: 529.9 KB\n"
     ]
    }
   ],
   "source": [
    "## information\n",
    "heart_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fb3c0bc6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:52.815859Z",
     "iopub.status.busy": "2022-03-20T16:29:52.815174Z",
     "iopub.status.idle": "2022-03-20T16:29:52.869282Z",
     "shell.execute_reply": "2022-03-20T16:29:52.869783Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.418116Z"
    },
    "papermill": {
     "duration": 0.137341,
     "end_time": "2022-03-20T16:29:52.869960",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.732619",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>male</th>\n",
       "      <th>age</th>\n",
       "      <th>education</th>\n",
       "      <th>currentSmoker</th>\n",
       "      <th>cigsPerDay</th>\n",
       "      <th>BPMeds</th>\n",
       "      <th>prevalentStroke</th>\n",
       "      <th>prevalentHyp</th>\n",
       "      <th>diabetes</th>\n",
       "      <th>totChol</th>\n",
       "      <th>sysBP</th>\n",
       "      <th>diaBP</th>\n",
       "      <th>BMI</th>\n",
       "      <th>heartRate</th>\n",
       "      <th>glucose</th>\n",
       "      <th>TenYearCHD</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4133.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4209.000000</td>\n",
       "      <td>4185.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4188.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "      <td>4219.000000</td>\n",
       "      <td>4237.000000</td>\n",
       "      <td>3850.000000</td>\n",
       "      <td>4238.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.429212</td>\n",
       "      <td>49.584946</td>\n",
       "      <td>1.978950</td>\n",
       "      <td>0.494101</td>\n",
       "      <td>9.003089</td>\n",
       "      <td>0.029630</td>\n",
       "      <td>0.005899</td>\n",
       "      <td>0.310524</td>\n",
       "      <td>0.025720</td>\n",
       "      <td>236.721585</td>\n",
       "      <td>132.352407</td>\n",
       "      <td>82.893464</td>\n",
       "      <td>25.802008</td>\n",
       "      <td>75.878924</td>\n",
       "      <td>81.966753</td>\n",
       "      <td>0.151958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.495022</td>\n",
       "      <td>8.572160</td>\n",
       "      <td>1.019791</td>\n",
       "      <td>0.500024</td>\n",
       "      <td>11.920094</td>\n",
       "      <td>0.169584</td>\n",
       "      <td>0.076587</td>\n",
       "      <td>0.462763</td>\n",
       "      <td>0.158316</td>\n",
       "      <td>44.590334</td>\n",
       "      <td>22.038097</td>\n",
       "      <td>11.910850</td>\n",
       "      <td>4.080111</td>\n",
       "      <td>12.026596</td>\n",
       "      <td>23.959998</td>\n",
       "      <td>0.359023</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>107.000000</td>\n",
       "      <td>83.500000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>15.540000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>42.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>206.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>75.000000</td>\n",
       "      <td>23.070000</td>\n",
       "      <td>68.000000</td>\n",
       "      <td>71.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>234.000000</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>82.000000</td>\n",
       "      <td>25.400000</td>\n",
       "      <td>75.000000</td>\n",
       "      <td>78.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>56.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>263.000000</td>\n",
       "      <td>144.000000</td>\n",
       "      <td>89.875000</td>\n",
       "      <td>28.040000</td>\n",
       "      <td>83.000000</td>\n",
       "      <td>87.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>696.000000</td>\n",
       "      <td>295.000000</td>\n",
       "      <td>142.500000</td>\n",
       "      <td>56.800000</td>\n",
       "      <td>143.000000</td>\n",
       "      <td>394.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              male          age    education  currentSmoker   cigsPerDay  \\\n",
       "count  4238.000000  4238.000000  4133.000000    4238.000000  4209.000000   \n",
       "mean      0.429212    49.584946     1.978950       0.494101     9.003089   \n",
       "std       0.495022     8.572160     1.019791       0.500024    11.920094   \n",
       "min       0.000000    32.000000     1.000000       0.000000     0.000000   \n",
       "25%       0.000000    42.000000     1.000000       0.000000     0.000000   \n",
       "50%       0.000000    49.000000     2.000000       0.000000     0.000000   \n",
       "75%       1.000000    56.000000     3.000000       1.000000    20.000000   \n",
       "max       1.000000    70.000000     4.000000       1.000000    70.000000   \n",
       "\n",
       "            BPMeds  prevalentStroke  prevalentHyp     diabetes      totChol  \\\n",
       "count  4185.000000      4238.000000   4238.000000  4238.000000  4188.000000   \n",
       "mean      0.029630         0.005899      0.310524     0.025720   236.721585   \n",
       "std       0.169584         0.076587      0.462763     0.158316    44.590334   \n",
       "min       0.000000         0.000000      0.000000     0.000000   107.000000   \n",
       "25%       0.000000         0.000000      0.000000     0.000000   206.000000   \n",
       "50%       0.000000         0.000000      0.000000     0.000000   234.000000   \n",
       "75%       0.000000         0.000000      1.000000     0.000000   263.000000   \n",
       "max       1.000000         1.000000      1.000000     1.000000   696.000000   \n",
       "\n",
       "             sysBP        diaBP          BMI    heartRate      glucose  \\\n",
       "count  4238.000000  4238.000000  4219.000000  4237.000000  3850.000000   \n",
       "mean    132.352407    82.893464    25.802008    75.878924    81.966753   \n",
       "std      22.038097    11.910850     4.080111    12.026596    23.959998   \n",
       "min      83.500000    48.000000    15.540000    44.000000    40.000000   \n",
       "25%     117.000000    75.000000    23.070000    68.000000    71.000000   \n",
       "50%     128.000000    82.000000    25.400000    75.000000    78.000000   \n",
       "75%     144.000000    89.875000    28.040000    83.000000    87.000000   \n",
       "max     295.000000   142.500000    56.800000   143.000000   394.000000   \n",
       "\n",
       "        TenYearCHD  \n",
       "count  4238.000000  \n",
       "mean      0.151958  \n",
       "std       0.359023  \n",
       "min       0.000000  \n",
       "25%       0.000000  \n",
       "50%       0.000000  \n",
       "75%       0.000000  \n",
       "max       1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## stats\n",
    "heart_df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c84fa2cb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:53.043216Z",
     "iopub.status.busy": "2022-03-20T16:29:53.042419Z",
     "iopub.status.idle": "2022-03-20T16:29:53.051597Z",
     "shell.execute_reply": "2022-03-20T16:29:53.050969Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.484033Z"
    },
    "papermill": {
     "duration": 0.098409,
     "end_time": "2022-03-20T16:29:53.051753",
     "exception": false,
     "start_time": "2022-03-20T16:29:52.953344",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male               0.000472\n",
       "age                0.009202\n",
       "education          0.000944\n",
       "currentSmoker      0.000472\n",
       "cigsPerDay         0.007787\n",
       "BPMeds             0.000472\n",
       "prevalentStroke    0.000472\n",
       "prevalentHyp       0.000472\n",
       "diabetes           0.000472\n",
       "totChol            0.058518\n",
       "sysBP              0.055215\n",
       "diaBP              0.034450\n",
       "BMI                0.321614\n",
       "heartRate          0.017225\n",
       "glucose            0.033742\n",
       "TenYearCHD         0.000472\n",
       "dtype: float64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## unique values\n",
    "heart_df.nunique()/heart_df.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d548d1ed",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:53.217345Z",
     "iopub.status.busy": "2022-03-20T16:29:53.216396Z",
     "iopub.status.idle": "2022-03-20T16:29:53.223804Z",
     "shell.execute_reply": "2022-03-20T16:29:53.224400Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.500018Z"
    },
    "papermill": {
     "duration": 0.091881,
     "end_time": "2022-03-20T16:29:53.224576",
     "exception": false,
     "start_time": "2022-03-20T16:29:53.132695",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male                 0\n",
       "age                  0\n",
       "education          105\n",
       "currentSmoker        0\n",
       "cigsPerDay          29\n",
       "BPMeds              53\n",
       "prevalentStroke      0\n",
       "prevalentHyp         0\n",
       "diabetes             0\n",
       "totChol             50\n",
       "sysBP                0\n",
       "diaBP                0\n",
       "BMI                 19\n",
       "heartRate            1\n",
       "glucose            388\n",
       "TenYearCHD           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## null values\n",
    "heart_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbf9658a",
   "metadata": {
    "papermill": {
     "duration": 0.081314,
     "end_time": "2022-03-20T16:29:53.387303",
     "exception": false,
     "start_time": "2022-03-20T16:29:53.305989",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **DATA CLEANING**\n",
    "\n",
    "> Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6c9bc83e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:53.554298Z",
     "iopub.status.busy": "2022-03-20T16:29:53.553334Z",
     "iopub.status.idle": "2022-03-20T16:29:53.562870Z",
     "shell.execute_reply": "2022-03-20T16:29:53.563430Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.51321Z"
    },
    "papermill": {
     "duration": 0.094856,
     "end_time": "2022-03-20T16:29:53.563619",
     "exception": false,
     "start_time": "2022-03-20T16:29:53.468763",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Replacing null values with the mean value\n",
    "heart_df[\"education\"].fillna(heart_df[\"education\"].mean(),inplace=True)\n",
    "heart_df[\"cigsPerDay\"].fillna(heart_df[\"cigsPerDay\"].mean(),inplace=True)\n",
    "heart_df[\"BPMeds\"].fillna(heart_df[\"BPMeds\"].mean(),inplace=True)\n",
    "heart_df[\"totChol\"].fillna(heart_df[\"totChol\"].mean(),inplace=True)\n",
    "heart_df[\"BMI\"].fillna(heart_df[\"BMI\"].mean(),inplace=True)\n",
    "heart_df[\"heartRate\"].fillna(heart_df[\"heartRate\"].mean(),inplace=True)\n",
    "heart_df[\"glucose\"].fillna(heart_df[\"glucose\"].mean(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e1da38fc",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:53.730920Z",
     "iopub.status.busy": "2022-03-20T16:29:53.729938Z",
     "iopub.status.idle": "2022-03-20T16:29:53.737540Z",
     "shell.execute_reply": "2022-03-20T16:29:53.737984Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.529719Z"
    },
    "papermill": {
     "duration": 0.092869,
     "end_time": "2022-03-20T16:29:53.738155",
     "exception": false,
     "start_time": "2022-03-20T16:29:53.645286",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male               0\n",
       "age                0\n",
       "education          0\n",
       "currentSmoker      0\n",
       "cigsPerDay         0\n",
       "BPMeds             0\n",
       "prevalentStroke    0\n",
       "prevalentHyp       0\n",
       "diabetes           0\n",
       "totChol            0\n",
       "sysBP              0\n",
       "diaBP              0\n",
       "BMI                0\n",
       "heartRate          0\n",
       "glucose            0\n",
       "TenYearCHD         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Rechecking for null values\n",
    "heart_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5907359a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:29:53.907061Z",
     "iopub.status.busy": "2022-03-20T16:29:53.906077Z",
     "iopub.status.idle": "2022-03-20T16:29:53.913388Z",
     "shell.execute_reply": "2022-03-20T16:29:53.912862Z",
     "shell.execute_reply.started": "2022-03-20T15:06:57.552332Z"
    },
    "papermill": {
     "duration": 0.09385,
     "end_time": "2022-03-20T16:29:53.913540",
     "exception": false,
     "start_time": "2022-03-20T16:29:53.819690",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    3594\n",
       "1     644\n",
       "Name: TenYearCHD, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## CHD value counts\n",
    "heart_df.TenYearCHD.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8300c61",
   "metadata": {
    "papermill": {
     "duration": 0.10975,
     "end_time": "2022-03-20T16:30:05.452582",
     "exception": false,
     "start_time": "2022-03-20T16:30:05.342832",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **SPLITTING DATA - TRAINING AND TESTING SETS**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bb7c10bb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:30:05.679882Z",
     "iopub.status.busy": "2022-03-20T16:30:05.679013Z",
     "iopub.status.idle": "2022-03-20T16:30:05.945230Z",
     "shell.execute_reply": "2022-03-20T16:30:05.945799Z",
     "shell.execute_reply.started": "2022-03-20T15:07:02.474289Z"
    },
    "papermill": {
     "duration": 0.382049,
     "end_time": "2022-03-20T16:30:05.945998",
     "exception": false,
     "start_time": "2022-03-20T16:30:05.563949",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## importing packages\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix , classification_report,accuracy_score\n",
    "from sklearn.metrics import roc_curve , auc\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "946c31f6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:30:06.173915Z",
     "iopub.status.busy": "2022-03-20T16:30:06.173160Z",
     "iopub.status.idle": "2022-03-20T16:30:06.182361Z",
     "shell.execute_reply": "2022-03-20T16:30:06.182845Z",
     "shell.execute_reply.started": "2022-03-20T15:07:02.563316Z"
    },
    "papermill": {
     "duration": 0.122937,
     "end_time": "2022-03-20T16:30:06.183028",
     "exception": false,
     "start_time": "2022-03-20T16:30:06.060091",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Columns in X : Index(['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',\n",
      "       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',\n",
      "       'diaBP', 'BMI', 'heartRate', 'glucose'],\n",
      "      dtype='object')\n",
      "y : 0       0\n",
      "1       0\n",
      "2       0\n",
      "3       1\n",
      "4       0\n",
      "       ..\n",
      "4233    1\n",
      "4234    0\n",
      "4235    0\n",
      "4236    0\n",
      "4237    0\n",
      "Name: TenYearCHD, Length: 4238, dtype: int64\n",
      "shape of X: (4238, 15)\n",
      "shape of y: 4238\n"
     ]
    }
   ],
   "source": [
    "## Defining variables X,y \n",
    "X= heart_df.drop(\"TenYearCHD\",axis=1)\n",
    "y=heart_df[\"TenYearCHD\"]\n",
    "print(\"Columns in X :\",X.columns)\n",
    "print(\"y :\",y)\n",
    "print(\"shape of X:\",X.shape)\n",
    "print(\"shape of y:\",y.shape[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "842e0816",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:30:06.410361Z",
     "iopub.status.busy": "2022-03-20T16:30:06.409625Z",
     "iopub.status.idle": "2022-03-20T16:30:06.415309Z",
     "shell.execute_reply": "2022-03-20T16:30:06.415827Z",
     "shell.execute_reply.started": "2022-03-20T15:07:02.580457Z"
    },
    "papermill": {
     "duration": 0.121444,
     "end_time": "2022-03-20T16:30:06.415994",
     "exception": false,
     "start_time": "2022-03-20T16:30:06.294550",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Splitting data into training and test sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5e4f185",
   "metadata": {
    "papermill": {
     "duration": 0.112454,
     "end_time": "2022-03-20T16:30:06.641209",
     "exception": false,
     "start_time": "2022-03-20T16:30:06.528755",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **MODEL TRAINING**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "41eebb4e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:30:06.904768Z",
     "iopub.status.busy": "2022-03-20T16:30:06.904020Z",
     "iopub.status.idle": "2022-03-20T16:30:06.921640Z",
     "shell.execute_reply": "2022-03-20T16:30:06.922299Z",
     "shell.execute_reply.started": "2022-03-20T15:07:02.593842Z"
    },
    "papermill": {
     "duration": 0.157275,
     "end_time": "2022-03-20T16:30:06.922491",
     "exception": false,
     "start_time": "2022-03-20T16:30:06.765216",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "## Scaling the data \n",
    "sc= StandardScaler()\n",
    "X_train = sc.fit_transform(X_train)\n",
    "X_test=sc.transform(X_test)\n",
    "X_train=pd.DataFrame(X_train,columns=X.columns)\n",
    "X_test=pd.DataFrame(X_test,columns=X.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "616a5e9f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-03-20T16:30:07.180803Z",
     "iopub.status.busy": "2022-03-20T16:30:07.180089Z",
     "iopub.status.idle": "2022-03-20T16:30:07.235560Z",
     "shell.execute_reply": "2022-03-20T16:30:07.236545Z",
     "shell.execute_reply.started": "2022-03-20T15:07:02.611849Z"
    },
    "papermill": {
     "duration": 0.191142,
     "end_time": "2022-03-20T16:30:07.236826",
     "exception": false,
     "start_time": "2022-03-20T16:30:07.045684",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Training the model using Logistic Regression\n",
    "regressor=LogisticRegression()\n",
    "regressor.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2ebc7985",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "87cae110",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "file_name='heart_prediction.pkl'\n",
    "f = open(file_name,'wb')\n",
    "pickle. dump(regressor,f)\n",
    "f. close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d3d509be",
   "metadata": {},
   "outputs": [],
   "source": [
    "heart_prediction = pickle.load(open('heart_prediction.pkl','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2570363",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 41.084218,
   "end_time": "2022-03-20T16:30:21.419970",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-03-20T16:29:40.335752",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
