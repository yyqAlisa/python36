import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs  #创建成团的数据
from sklearn.cluster import KMeans


#1.产生数据
N = 1000
n_centers = 4
X, Y = make_blobs(n_samples=N, n_features=2, centers=n_centers, random_state=14)
print(X.shape)
print(Y.shape)

#数据的可视化一下
plt.scatter(X[:, 0], X[:, 1], c=Y, s=30)
plt.show()

#2.Kmeans模型构建
model = KMeans(n_clusters=4)
model.fit(X, Y)

#3.输出模型得到的中心点和目标函数的损失值
print('中心点坐标')
print(model.cluster_centers_)
print('目标函数的损失值（所有样本到对应簇中心点的的距离平方和）:')
print(model.inertia_)
print(model.inertia_/N)

#4.预测
y_hat = model.predict(X[:10])
print('预测值:{}'.format(y_hat))
print('实际值:{}'.format(Y[:10]))
print('模型的Score评估值:{}'.format(model.score(X, Y)))