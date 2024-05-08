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
2. Data preprocessing and cleaning: Load the [dataset](telco_customer_churn.csv) and clean it.
3. Exploratory data analysis: Find patterns in the dataset. We try to analyze different factors which affect the target variable(churn column) and the extent to which it does so.
4. Model Building: evaluate the best machine learning algorithm to identify complex patterns in the data.

## Conclusion

- In conclusion, we have drawn the following observations from the data.
- That;
    1. ...
