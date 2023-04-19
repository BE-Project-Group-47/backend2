# A Comparative Study of ML Classifiers in Credit Risk Analysis

### Group No: 47

### Members
- Jay Bhavsar
- Parth Cheulkar
- Mihir Chhabria
- Tanya Chandnani

### Abstract
One of the most crucial tasks in the financial sector is decision-making. There are many risks involved in a loan or credit approval system. Credit risk is the possibility of a loss resulting from a borrower's failure to repay a loan or meet contractual obligations. Credit risks are calculated based on the borrower's overall ability to repay a loan according to its original terms. To assess credit risk on a consumer loan, lenders look at the five C’s: credit history, capacity to repay, capital, the loan's conditions, and associated collateral. Companies have established departments solely responsible for analyzing the credit score of their current and potential customers. This project aims at comparing the use of machine learning classifiers used in this process of risk calculation. Based on a real-life dataset, we will be observing how the accuracy and performance vary based on different algorithms used for classification. We will also be building a tool for a generic user to be able to visualize the use of different algorithms used for generating risk factors.

### Algorithms Used:
- Naive Bayes
- K-Nearest Neighbors
- Decision Tree
- Logistic Regression
- Multilayer Perceptron (ANN)
- Ensemble-Stacking
- Ensemble-Bagging (using Random Forest)
- Ensemble-Boosting(using XGBoost)

### Project Setup

> Backend 
```
# first initialise virtual environment after cloning
virtualenv env
.env\Scripts\activate

# install dependencies
pip install -r requirements.txt

# locate the manage.py file
cd bank
python manage.py migrate
python manage.py runserver

# Backend is up and runnning
```
> Frontend
```
# after cloning make sure to have npm installed on your device
npm install
npm run start

# Frontend is up and runnning
```

## Classifier results (based on Comparative Analysis)


|Classifier |Accuracy |Recall |F1-score |Precision | ROC_AUC Score | 
|:----------|:--------|:------|:--------|:---------|:--------------|
|Logistic Regression |0.84 |0.45 |0.56 |0.72 |0.85|
|Decision Tree |0.92 |0.80 |0.70 |0.92 |0.91|
|Gaussian Naive Bayes|0.82|0.64|0.61|0.58|0.85|
|K-Nearest Neighbors| 0.85|0.40|0.64|0.85|0.88
|ANN| 0.91| 0.69|0.78|0.89|0.91
|Ensemble - Stacking|0.91|0.71|0.77|0.85|0.90
|Ensemble- Bagging| 0.93|0.71|0.82|0.96|0.93|
|Ensemble- Boosting|0.93|0.73|0.83|0.96|0.95

