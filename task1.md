# Exam in ML

## Task 1

> what are some causes of overfitting how do we diagnose and treat overfitting in regression models?

Some reasons for overfitting depends on what kind of models you are doing, but in regression models it happens when our model is too complex. If we give our models to many parameters and not enough data, it will be very good at predicting our training data, but not creating a good generalized way to predict new data.

One way to see if our model is overfitted, is to visualize our model and see if the curve of our predictions is weird, maybe very sigsagy - instead of just running a line thru some datapoints, it'll actually hit all of them.

To reduce overfitting, one thing you can do, is reduce the number of parameters to match with the quantity of our data. One thing that might have happened, is the model used noice as part of predictions. 

another way to reduce overfitting is to include more data than you already have. Some problems need more data than others, and it may vary based on dimentions of your data.


## Task 2

> What is difference between L1 and L2 regularization?


