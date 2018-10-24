# Starting time
startTime <- proc.time()

# load the package
library(C50)

# load data
X2 <- read.csv("321.csv", header = TRUE);

# omitting null values
X2 = na.omit(X2)

# fit model
fit <- C5.0(higher~., data=X2)

# summarize the fit
print(fit)

# make predictions
predictions <- predict(fit, X2)

# summarize accuracy
table_val <- table(predictions, X2$higher)

# displaying table
table_val

# finding accuracy and displaying it
y <- "%"
paste(c((sum(diag(table_val))/sum(X) * 100 ) , y), collapse = " ")

# write the confusion matrix
write.table(table_val,"result.txt",sep="\t",row.names=FALSE)

# plotting the values
plot(predictions, main="C5.0 Plot", ylab = "Numbers", xlab="Target Column Values")

# time consumed
proc.time() - startTime

