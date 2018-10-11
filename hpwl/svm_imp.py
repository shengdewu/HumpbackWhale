from hpwl.perceptron import perceptron
from sklearn import svm

class svm_imp(perceptron):

    def train(self, x, y):
        self.__svm__.fit(x, y)
        print(str('train percision {0}').format(round(self.__svm__.score(x, y)*100, 3)))
        return

    def predict(self, x):
        y = self.__svm__.predict(x)
        return y

    def __init__(self):
        super(svm_imp, self).__init__()
        self.__svm__ = svm.SVC(C=2.0, kernal='rbf', gamma=0.0001)
        return