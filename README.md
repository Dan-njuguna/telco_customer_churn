# Telco Customer Churn

## Authors

1. [Dan Njuguna](mailto:njugunaadan@gmail.com)
2. [Sumbati Lindah](mailto:sumbatilinda@gmail.com)

## About the Dataset

- The dataset [telco_customer_churn.csv](telco_customer_churn.csv) has information about how company churns its customers depending on various factors.
- A predictive model is made out of the dataset with the following column information.

| Column Name | Data Type | Description   |
| ---------- | -------- | -------------- |
| customerID | object |  A unique ID that identifies each customer.  |
| gender | object | The customer’s gender: Male, Female |
| SeniorCitizen | integer | Indicates if the customer is 65 or older: (1, 0) |
| Partner | object | Indicates if the customer is married: Yes, No |
| Dependents | object | whether the customer has dependents or not (Yes, No). A dependent is a person who relies on another as a primary source of income, |
| tenure | integer | number of months the customer has stayed with the company |
| PhoneService | object | whether the customer has a phone service or not (Yes, No) |
| MultipleLines | object | whether the customer has multiple lines or not (Yes, No, No phone service) |
| InternetService | object | customer’s internet service provider (DSL, Fiber optic, No) |
| OnlineSecurity | object | whether the customer has online security or not (Yes, No, No internet service) |
| OnlineBackup | object | whether the customer has online backup or not (Yes, No, No internet service) |
| DeviceProtectio | object | whether the customer has device protection or not (Yes, No, No internet service) |
| TechSupport | object | whether the customer has tech support or not (Yes, No, No internet service) |
| StreamingTV | object | whether the customer has streaming TV or not (Yes, No, No internet service) |
| StreamingMovies | object | whether the customer has streaming movies or not (Yes, No, No internet service) |
| Contract | object | type of contract according to duration (Month-to-month, One year, Two year) |
| PaperlessBilling | object | bills issued in paperless form (Yes, No) |
| PaymentMethod | object | payment method used by customer (Electronic check, Mailed check, Credit card (automatic), Bank transfer (automatic)) |
| MonthlyCharge | integer | amount of charge for service on monthly bases |
| TotalCharges | integer | cumulative charges for service during subscription (tenure) period |
| churn | object | output value, predict variable(yes or no) |

## Problem Statement

- From the data given, we wish to _Predict behavior to retain customers_ by the company. Thereore, we will derive insight from the columns given and predict the customer was churned or not.

## Approaches Used

- To handle the data and create the model, the following methods have been employed in out project:

  1. Data Understanding: Understand the dataset and the problem statement.
  2. Exploratory data analysis and cleaning: Load the [dataset](telco_customer_churn.csv) and clean it. Find patterns in the dataset. We try to analyze different factors which affect the target variable(churn column) and the extent to which it does so.
  3. Statistical analysis and testing: We create hypothesis to spot correlation between given features in the data.
  4. Feature Engineering: creating new features or transforming existing features to improve the performance of a machine-learning model.
  5. Model Building: evaluate the best machine learning algorithm to identify complex patterns in the data.

## Observations Made

- During EDA, we found that the TotalCharges column was an object datatype column and converted it to numeric. The column contains numeracal values.
- Further, it is notable that there are no outliers in the dataset, since all the values for all numerical columns remain within IQR.
- Finding the unique values for each categorical column so that we are in position to understand the data we will be encoding(to numeric using LabelEncoder())
- We have also observed in the visualisations the counts of various columns with relation to the Churn column. This includes the _Gender_ column: Where we highlited the numbers of females and males who have been churned by the telco.
- From the stastistical modelling of the data, we can draw the following observations:

  - There is no significant difference in the proportion of churned customers between female and male groups.
  - There is an association between customer churn and having a Month-to-Month contract.
  - There is an association between customer churn and internet service type.

- We encode all categorical columns to numeric using the function shown below:

```Python
def encode_column(df, col):
  """
  Encodes a single categorical column in a pandas dataframe using LabelEncoder.

  Args:
      df (pandas.DataFrame): The dataframe containing the column to encode.
      col (str): The name of the column to encode.

  Returns:
      pandas.DataFrame: The dataframe with the encoded column.
  """
  encoder = LabelEncoder()
  df[col] = encoder.fit_transform(df[col])
  return df
```

- Which, using LabelEncoder, every categorical columns' unique value are assigned a unique integer and then the function returns a dataframe that has been encoded and no remaining categorical column.

- The correlation matrix shows the pairwise correlation coefficients between different numerical features in the dataset after encoding.
- During visualisations, we observed that there was imbalance in the target column(_Churn_) which suggested that we had to oversample the dataset.
- We considered using RandomOverSampler for the dataset, and finetune the hypaparameters to reduce bias in the dataset.
- Using three models:
  - Logistic Regression
  - Random Forest Classifier
  - Support Vector Machine
- The models had an overrall good performance on the data after oversampling the data, with the recall and precision scores for both class(churn and non-churn) variables been within similar range.
- Generally, Random Forest Classifier performed the best on this dataset.
- The AUC-ROC of the models suggested close relationship in the area under curve for the Logistic regresssion and support vector machine models while the Random Forest Classifier had higher AUC.

## Conclusion

- In conclusion, we have drawn the following conclusions made from the observations of the data.
- That;
    1. There was no significant difference in the proportion of churned customers between female and male groups from the statistical hypothesis testing on the data.
    2. There was a relationship between customer churn and having a Month-to-Month contract(tenure) from the hypothesis testing.
    3. There was a relationship between customer churn and internet service type which suggests that the internet service type is directly related with the customer churn information.
    4. It was possible to predict whether a customer was churned or not from any of the three models, where RandomForestClassifier had the best accuracy in predicting the customer churn.
    5. AUC-ROC relationship was important to the accuracy of the model, an that the area under curve is directly proportional to the model accuracy.

## Using this Model

- To use this model on your local machine machine, open the bash terminal(Linux CLI) and clone the repository as follows:

```bash
git clone https://github.com/Dan-njuguna/telco_customer_churn.git
```

- After you have successfully cloned the repository on your local machine open Vscode(Personal preference) in the current directory(Repository cloned):

```bash
cd telco_customer_churn
code .
```

- You can now run the cells on your Jupyter Notebook environment.😊

## Pattent Rights

- This work is entirely the intelectual property of the **AUTHORS**: Lindah Sumbati and Dan Njuguna.
- However, use of the files and the code is allowed for all. Enjoy your learning!

# **EOF**
