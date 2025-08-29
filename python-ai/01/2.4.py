from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建并训练模型
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# 预测并评估
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))