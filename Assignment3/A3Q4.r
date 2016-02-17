y <- c(0,0,0,0,0,0,0,0,1,1) 
x <- c(0.000985,0.000127,0.000171,0.000062,0.000812,0.00443,0.00007,0.000069,0.000399,0.000104) 

ylab = 'y' 
xlab = 'x'  

library('Kendall') 
k <- Kendall(x,y) 

plot(x,y,main='Scatterplot',xlab=xlab,ylab=ylab) 
grid() 
dev.off() 

plot(rank(x),rank(y),main='Scatterplot of Ranks',xlab=xlab,ylab=ylab) 
grid() 
dev.off() 

a<-table.start() 
a<-table.row.start(a) 
a<-table.element(a,'Kendall tau Rank Correlation',2,TRUE)
a<-table.row.end(a) 

a<-table.row.start(a) 
a<-table.element(a,'Kendall tau',header=TRUE) 
a<-table.element(a,k$tau) 
a<-table.row.end(a) 

a<-table.row.start(a) 
a<-table.element(a,'p-value',header=TRUE) 
a<-table.element(a,k$sl) 
a<-table.row.end(a) 

a<-table.row.start(a) 
a<-table.element(a,'Score',header=TRUE) 
a<-table.element(a,k$S) 
a<-table.row.end(a)

a<-table.row.start(a) 
a<-table.element(a,'Var(Score)',header=TRUE) 
a<-table.element(a,k$varS) 
a<-table.row.end(a) 

a<-table.row.start(a) 
a<-table.element(a,'Denominator',header=TRUE) 
a<-table.element(a,k$D) 
a<-table.row.end(a) 

a<-table.end(a) 
