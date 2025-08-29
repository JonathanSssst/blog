import numpy as np

# Sigmoid激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 神经网络前向传播
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化权重
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.1
        self.b2 = np.zeros((1, output_size))
    
    def forward(self, X):
        # 第一层
        self.z1 = X @ self.W1 + self.b1
        self.a1 = sigmoid(self.z1)
        
        # 第二层
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = sigmoid(self.z2)
        
        return self.a2
    
    def predict(self, X):
        return np.round(self.forward(X))

# 创建网络并进行预测
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # XOR问题
nn = SimpleNeuralNetwork(2, 3, 1)
predictions = nn.forward(X)
print("网络输出:")
print(predictions)