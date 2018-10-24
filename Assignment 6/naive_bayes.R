# Starting time
startTime <- proc.time()

# importing library
library(e1071)

# reading csv file
X2 <- read.csv("321.csv", header = TRUE);

# omitting null values
X2 = na.omit(X2)

# naive bayes model
m <- naiveBayes(higher~ ., data = X2)

# predicting output
NB_Predictions=predict(m,X2)

# predicted table
X <- table(NB_Predictions,X2$higher)

# displaying table
X 

# finding accuracy and displaying it
y <- "%"
paste(c((sum(diag(X))/sum(X) * 100 ) , y), collapse = " ")

# write the confusion matrix
write.table(X,"result.txt",sep="\t",row.names=FALSE)

# plotting the values
plot(NB_Predictions, main="Naive Bayes Plot", ylab = "Numbers", xlab="Target Column Values")

# time consumed
proc.time() - startTime

