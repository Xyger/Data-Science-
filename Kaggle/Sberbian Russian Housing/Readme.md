# Sberbian Russian Housing
The problem is to predict realty prices in the housing market of Russia.Given a very broad spectrum of features,in addition with the information of Russian economic and macroeconomics patterns,this requires heavy analysis of features,deciding which  features become the functional characteristics in accurately predicting the housing prices.<br>The dataset consists of 30,500 training rows and around 7800 test rows and the evaluation metric is Root-mean-squared-error.<br >

The key points in my problem approach and modelling are:
* Separated the training set on the 'product_type' as it improved my score a lot.
* Trained XGBoost sepately on the two training sets.But,it seems that for 'product_type' =='Investment',training on the whole training set gave better overall predictions for investment type homes.
* For the 'OwnerOccupier' type,I have used 'price_per_sq_m' instead of 'price_doc' which improved my score much.Also this seems quite reasonable to estimate the quality or expensiveness in price/square_metre of houses.
* To overcome CV problem using GridSearch and hyperparameter tuning to increase score,I trained 100 XGBoosts models with comparatively less estimators and averaged across them to get my price predicted.
* I have used cleaned and corrected dataset as there were many such absurd values.I got this from the kernel (https://www.kaggle.com/c/sberbank-russian-housing-market/discussion/34364)
* Some new features were created like 'relative living area' , 'dayBought-daybuilt','life_sq/num_rooms','Total distance to basic amenities' etc.
