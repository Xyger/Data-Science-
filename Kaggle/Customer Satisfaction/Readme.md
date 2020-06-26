# Santander's Customer Satisfaction

The problem statement can be found [here](https://www.kaggle.com/c/santander-customer-satisfaction).
We are provided with a whole lot of anonymised features which are either categorical or numerical.The variable to predict is
the TARGET column(0 or 1). The dataset has 152k training rows and around 740 columns.The evaluation metric has been Area under ROC curve ,instead of accuracy score or logloss score.
#### **Tools** : *pandas, numpy, sklearn, matplotlib, seaborn ,xgboost*
A basic random forest was used to gain knowlegde of mist important features initially.
Then various features pairwise correlation with the TARGET variable was done.
As these features were anonymised,I came to know what these variables actually represent from the 
discussion forum on Kaggle,which further helped me to understand this problem.
At last,XGboost classifier was used to predict the satisfaction variable which got me a public LB of 0.83812
