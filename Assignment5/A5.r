library(igraph)

#creates a Zachary Graph
karate <- make_graph("Zachary")

#2 Communities
group<-label.propagation.community(karate)
plot(group, karate)

# 3 Communities
group1<-fastgreedy.community(karate)
plot(group1, karate)

# 4 Communities
group2<-Springlass.community(karate)
plot(group2, karate)

# 5 Communities
group3<-walktrap.community(karate)
plot(group3, karate)