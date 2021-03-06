from util import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

print 'Reading files'
np_data = read_file()
print 'Separate X and Y'
[X, Y] = separate_X_Y(np_data)
print 'Getting set of outputs'

[X_f, Y_no_transform, Y_equal_size, Y_equal_frequency] = pre_process(X, Y)
len_train = int(2.0*float(len(X_f))/3.0)
X_f = X_f[:len_train]
Y_no_transform = Y_no_transform[:len_train]
Y_equal_size = Y_equal_size[:len_train]
Y_equal_frequency = Y_equal_frequency[:len_train]

scores_1 = []
scores_2 = []

Ks = []
for i in xrange(50):
    K = 2*i + 1
    print i+1, 'of 50'
    knn_classifier_1 = KNeighborsClassifier(n_neighbors=K, weights='uniform')
    knn_classifier_2 = KNeighborsClassifier(n_neighbors=K, weights='distance')
    
    new_score_1 = np.mean(cross_val_score(knn_classifier_1, X_f, Y_equal_frequency, cv=3))
    new_score_2 = np.mean(cross_val_score(knn_classifier_2, X_f, Y_equal_frequency, cv=3))
    
    Ks.append(K)
    scores_1.append(new_score_1)
    scores_2.append(new_score_2)
    
plt.xlabel('Valor de K')
plt.ylabel('Acuracia media - 3 fold')
uniform, = plt.plot(Ks, scores_1, 'b', label='uniform')
distance, = plt.plot(Ks, scores_2, 'r', label='distance')

plt.legend([uniform, distance], ['uniform', 'distance'])
plt.show()
