# New York TaxiFare Challenge
The problem statement can be found [here](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). Given the information of every taxi travels in NewYork,we need to predict the taxi fare by using a supervised learning(regression).<br>
The dataset is very huge with 55M training rows and the metric is Root-Mean-Squared_Error.<br>
Following steps were taken before modelling:<br>
* The data is first corrected and many wrong entries has been dropped.Also,I have just used 2 million rows.
* The distance I have used is the Harvesine Distance.
* I have also considered these conditions :
  * Fare is 0 but distance is not.
  * Distance is 0 but fare is not.
  * Both distance and fare are zero.<br >
  
Then , a Random Forest model was fitted on, which gave me public score of 3.1983
