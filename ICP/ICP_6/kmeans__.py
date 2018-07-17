import pandas
# load all necessary libraries
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# loading data
variables = pandas.read_csv(r'C:\Users\bsidd\Downloads\Python_Lesson6\Python_Lesson6\sample_stocks.csv')
#load returns, dividendyield to x,y
Y = variables[['returns']]
X = variables[['dividendyield']]
# assume a cluster in range 1,20
Nc = range(1, 20)
# for every cluster calculate kmeans
kmeans = [KMeans(n_clusters=i) for i in Nc]

kmeans
# calculate score
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]

score
# plot the score and clusters
pl.plot(Nc,score)

pl.xlabel('Number of Clusters')

pl.ylabel('Score')

# use elbow curve to get the appropriate number of clusters
pl.title('Elbow Curve')

pl.show()
# use PCA to reduce dimensionality and interpret datapoints
pca = PCA(n_components=1).fit(Y)
# transform the x,y using PCA
pca_d = pca.transform(Y)

pca_c = pca.transform(X)
# here the best number of clusters is 3
kmeans=KMeans(n_clusters=3)
# fit data using kmeans
kmeansoutput=kmeans.fit(Y)

kmeansoutput

pl.figure('3 Cluster K-Means')
# scatter all datapoints into respective clusters
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')

pl.ylabel('Returns')
pl.show()
