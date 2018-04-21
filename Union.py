import data_utils as du
import sys
from sklearn.metrics import classification_report
import numpy as np

def convert_result(line):
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace("'", '')
    line = line.split(', ')
    return line

test_sentences, test_labels = du.sentences_to_lists("results/twitter_test_conll_format.txt")

lengths = [len(x) for x in test_sentences]

#test a
CRFa = open('results/twitter_CRF_result.txt', 'r')
RFa  = open('results/twitter_random_forest_result.txt', 'r')
bia = open ('results/twitter_bilstm_result.txt', 'r')
#problem retrieving list from files
crf_result = str(CRFa.readline())
crf_result = convert_result(crf_result)
rf_result = str(RFa.readline())
rf_result = convert_result(rf_result)
bi_result = str(bia.readline())
bi_result = convert_result(bi_result)

#.split(', ')



print(len(crf_result))
#print((crf_result))
print(len(rf_result))
#print((rf_result))
print(len(bi_result))
#print((bi_result))
print((lengths))
#sys.exit()



i = 0
z = 0
w = 0
j = 0
best_results = []
for ind in range(len(crf_result)):
    flag = False
    print("CRF[{0}]:{1}  RF[{2}]: {3}  BiLSTM[{4}]: {5}".format(i, crf_result[i], i,  rf_result[i], z, bi_result[z]))
    #print("CRF:{0}  RF: {1}  BiLSTM: {2}".format(i, i, z))
    if((crf_result[i] == rf_result[i])):
        flag = True
        best_results.append(crf_result[i])
    elif ((crf_result[i] == bi_result[z])):
        flag = True
        best_results.append(crf_result[i])
    elif ((rf_result[i] == bi_result[z])):
        flag = True
        best_results.append(rf_result[i])
    elif (flag == False):  #no two best choices
        best_results.append(rf_result[i])
    i = i + 1
    z = z + 1
    w = w + 1

    if(w == lengths[j]):
        #z = (z+113)-w #conll
        z = (z+33)-w   #twitter
        j = j + 1
        w = 0
print(len(best_results))
print(test_labels[:5])

#test_labels = np.array(du.labels_to_integer(test_labels)) #conll
test_labels = np.array(du.tweets_to_integer(test_labels))  #tweets

print(test_labels[:5])

#test_labels = [du.integer_to_label(x) for x in test_labels] #conll
test_labels = [du.tweets_to_label(x) for x in test_labels]   #tweets
print(test_labels[:5])
report = classification_report(y_true=test_labels, y_pred=best_results)#, target_names= target_names)
print(report)