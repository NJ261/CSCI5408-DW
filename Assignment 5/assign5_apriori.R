# starting timer 
startTime <- proc.time() 

# reading CSV File
X2 <- read.csv("1.csv") 

# Importing library
library(arules)

# training classifier, providing min support and confidence
rules <- apriori(X2,parameter = list(supp = 0.3, conf = 0.5, target = "rules"))

# generating summary of the rules
summary(rules)

# inspecting the generated rules
inspect(rules)

# showing consumed time
proc.time() - startTime

# saving rules in csv file
write(rules, file = "output.csv", sep = ",", quote = TRUE, row.names = FALSE)

