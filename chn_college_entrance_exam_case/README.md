# Project Main Idea
The project is going to find the different factors that possiblely influence the score of the mock-exam taken from students, so that it can give some insights of the performance of students with similar consition.


# Case Milestone

1. check the dataset first, find abnormals to clean up, make sure the data good to use
2. extract interesting insights such as the relationships between each features and distributions
3. do a regression model to see if the model can predict '总分' well
4. it is possible to do a classification model based on '模拟考' to see whether students take it
5. avoid issue like overfitting/underfitting and improve model performance


# Notes

* Python version: 3.13
* no xgboost model because of current python version does not support libomp dependency
* logistic regression and svr do not perform better than a dummy model, random forest is the best so far
* hyperparameter tunning using GridSearchCV from sklearn
* classification is not done yet