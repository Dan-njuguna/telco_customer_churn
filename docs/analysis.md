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