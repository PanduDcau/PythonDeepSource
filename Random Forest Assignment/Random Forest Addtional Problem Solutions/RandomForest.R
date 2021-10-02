#installing Pre-request Packages
install.packages("stats")
install.packages("dplyr")
install.packages("randomForest")

#load required libraries
library(stats)
library(dplyr)
library(randomForest)

#loading the Data Objects
batsy = iris

#inspect Data
View(batsy)

#Variable Selection
str(batsy)

#Splitting data in Training Process and as well as Testing
#A Vector that has random sample of Training Values

black=sample(2,nrow(batsy),replace = TRUE ,prob = c(0.65,0.35))

#Let's do the Training
Training = batsy[black==1,]

#Testing Data
Testing= batsy[black==2,]

#Create Random Forest Model

RF = randomForest(Species~.,data = Training)

#Evaluating Model Accuracy
Species_Pred = predict(RF,Testing)
Testing$Species_Pred <- predict(RF,Testing)
TestSpec_pred = Species_Pred 
View(Testing)

#Building Confusion Matrix
CM = table(Testing$Species, Testing$Species_Pred)
length(Testing$Species)
#length(Testing$Species_Pred)
CM

classification_Accuracy = sum(diag(CM)/sum(CM))
classification_Accuracy

