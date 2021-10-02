#Classification Tree
install.packages(tree)
install.packages('caret')
library(caret)
library(tree)   #Importing libraries for Decision Tree Impelementation
batman <- read.csv("D:\\DC Universe\\Ucsc\\Third Year\\SCS 3201 Machine Learning\\CCPP\\Csv Files\\binary.csv")
batman$admit=ifelse(batman$admit == 0 , "No" , "Yes")
batman$admit<- as.factor(batman$admit)

set.seed(2)
#Training the Data in 200 iterations
train=sample(1:nrow(batman), 200)

#Creating a Test data Set
batman.test= batman[-train,]

#Creating Training Data Set
batman.train = batman[train,]

#Creating a Decision Tree using the Specific Columns
tree.batman = tree(admit~gre+gpa+rank,data  =batman.train)

#Confusion Matrix Implementation to find the Accuracy of the Data training
tree.pred=predict(tree.batman,batman.test[,-1], type="class")
table(tree.pred,batman.test$admit)
#Cmat <- confusionMatrix(data=batman.test[2,], reference = batman.train[2,])


#Pruning the Tree to Optimize the Data Set
set.seed(2)
cv.batman = cv.tree(tree.batman, FUN =prune.misclass)

#Plotting the Pruned Tree
plot(cv.batman$size, cv.batman$dev , type="b")
prune.batman = prune.misclass(tree.batman, best = 3)

#After Pruning the DataSet , implementing Confusion Matrix
tree.pred=predict(prune.batman,batman.test, type="class")
table(tree.pred,batman.test$admit)
plot(prune.batman);
text(prune.batman , pretty=0)

#Regression Tree
library(MASS)
set.seed(1)
train=sample(1:nrow(Boston), nrow(Boston)*0.6)
tree.boston=tree(medv~.,Boston, subset =train)
plot(tree.boston)
text(tree.boston)
title("This is a Random Tree")
yhat=predict(tree.boston, newdata =Boston [-train,])
boston.test=Boston[-train, "medv"]
mean((yhat -boston.test)^2)

#Using Boston method to improve accuracy in Regression Tree
cv.boston=cv.tree(tree.boston)
plot(cv.boston$size, cv.boston$dev ,main="Boston Size vs Dev", sub="Value Fluctuation",
     xlab="Boston Size", ylab="Boston Dev", type="b")
prune.boston=prune.tree(tree.boston, best = 4)
plot(prune.boston)
text(prune.boston)
yhat=predict(prune.boston, newdata= Boston [-train,])
mean((yhat -boston.test)^2)

#Random Forest and Bagging
#Bagging/Boostrap Aggregation used when
# improving unstable estimation or classification schemes new data Entered

library(randomForest) #importing Random Forest Libraries
set.seed(1)
bag.boston=randomForest(medv~.,data = Boston, subset = train, mtry =13,
                        importance=TRUE)
yhat.bag=predict(bag.boston, newdata=Boston [-train,])
mean((yhat.bag -boston.test)^2)
varImpPlot(bag.boston)

#Boosting in order to minimize the Biasing the combined model
#install.packages("gbm")

library(gbm)
boost.boston= gbm(medv~., data = Boston[train,], distribution="gaussian",
                  n.trees=4000, interaction.depth =4)
yhat.boost=predict(boost.boston, newdata= Boston[-train,], n.trees =4000)
mean((yhat.boost -boston.test)^2)
summary(boost.boston)

boost.boston=gbm(medv~., data= Boston [train,], distribution = "gaussian",
                 n.trees = 4000, interaction.depth = 4 , shrinkage =0.2)
yhat.boost=predict(boost.boston, newdata= Boston[-train,], n.trees =4000)
mean((yhat.boost -boston.test)^2)









