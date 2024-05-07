# Telco Customer Churn

- The dataset [telco_customer_churn.csv](telco_customer_churn.csv) has information about how company churns its customers depending on various factors.
- A predictive model is made out of the dataset with the following column information.

| Column Name | Data Type | Description   |
| ---------- | -------- | -------------- |
| customerID | object |  unique value identifying customer  |
| gender | object | whether the customer is a male or a female |
| SeniorCitizen | integer | whether the customer is a senior citizen or not (1, 0) |
| Partner | object | whether the customer has a partner or not (Yes, No) |
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
