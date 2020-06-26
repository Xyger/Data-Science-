# House Prices: Advanced Regression Techniques
The problem statement can be found [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

This was my first regression problem which requires excess statistical tools and analysis.The goal was to predict the housing sale prices given the amount of different features it has.
The dataset has around 160 columns and 1500 training rows and the evaluation metric is Root-Mean-Squared_Error(RMSE).

An extensive insights gaining was required.also there was a hell lot of missing values,which needs to be handled before fitting a model.
New features which seemed reasonable and which captures a great deal of information were created by combining given features.

I used several regression models:
* Lasso 
* Ridge
* GradientBoosting Regressor
* LightGBM
* XGBoost 
* Random Forest
* SVR
and stacked them,and kept adjusting their prediction weights accroding to accuracy to fnd the best model with high public LB.
At last,some magic number coefficients were used by some of hte best kernels on kaggle which I copied which got me on public LB with score 0.12665
