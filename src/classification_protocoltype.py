import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.decomposition import PCA

train_data = pd.read_csv('../dataset/training_label_protocoltype.csv', low_memory=False, encoding="gbk",index_col=0)
print(train_data.shape)

test_data = pd.read_csv('../dataset/testing_label_protocoltype.csv', low_memory=False,encoding="gbk",index_col=0)
print(test_data.shape)

# train_data = train_data.loc[train_data['Label'] != 0]
# test_data = test_data.loc[test_data['Label'] != 0]

train_label = train_data.iloc[:,77]
train_feature = train_data.iloc[:, 1:77]   #取前77列数据
test_label = test_data.iloc[:,77]
test_feature = test_data.iloc[:, 1:77]

train_feature = np.array(train_feature)
train_label = np.array(train_label).T
test_feature = np.array(test_feature)
test_label = np.array(test_label).T
print("训练数据准备完成！！")

pca = PCA(n_components=0.9)
pca.fit(train_feature)
train_feature = pca.transform(train_feature)
test_feature = pca.transform(test_feature)

model1 = tree.DecisionTreeClassifier()
# model1 = tree.ExtraTreeClassifier()
# model1 = RandomForestClassifier()
# model1 = SVC()
model1.fit(train_feature, train_label)
print("开始预测攻击类型")
pred = model1.predict(test_feature)
confix = confusion_matrix(test_label, pred)
print("confusion matrix:")
print(confix)
acc = accuracy_score(test_label, pred)
print("accuracy:", acc)
precision = precision_score(test_label, pred, average='macro')
print("precision:",precision)
recall = recall_score(test_label, pred, average='macro')
print("recall:", recall)
f1 = f1_score(test_label, pred, average='macro')
print("F1:", f1)