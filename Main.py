import graphviz
from sklearn import tree
import os

file_list = []
paths = []
folder = "/Users/Mitchell/Downloads/train"
for files in os.listdir(folder):
    # print file
    file_path = os.path.join(folder, files)
    paths.append(file_path)
    f = open(file_path, 'r')
    file_list.append(f.read())
    f.close()

words = []
for files in file_list:
    lines = files.split(' ')
    words.append(lines)

other_words = []
for stuff in words:
    for word in stuff:
        other_words.append(word)

other_words = set(other_words)
email_words = words
word_counts = []
i = 0
for email in email_words:
    word_counts.append([])
    for word in other_words:
        word_counts[i].append(email.count(word))
    i = i + 1

labels = []
for path in paths:
    if "spm" in path:
        labels.append(1)
    else:
        labels.append(0)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(word_counts, labels)

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("Emails")

# ------------------------------------------------------

file_list = []
paths = []
folder = "/Users/Mitchell/Downloads/test"
for files in os.listdir(folder):
    # print file
    file_path = os.path.join(folder, files)
    paths.append(file_path)
    f = open(file_path, 'r')
    file_list.append(f.read())
    f.close()

words = []
for files in file_list:
    lines = files.split(' ')
    words.append(lines)

# other_words = []
# for stuff in words:
#     for word in stuff:
#         other_words.append(word)
#
# other_words = set(other_words)
email_words = words
word_counts = []
i = 0
for email in email_words:
    word_counts.append([])
    for word in other_words:
        if word in other_words:
            word_counts[i].append(email.count(word))
    i = i + 1

labels = []
for path in paths:
    if "spm" in path:
        labels.append(1)
    else:
        labels.append(0)

predictions = clf.predict(word_counts)
#print predictions[2]

num_correct = 0
count = 0
for i in predictions:
    if predictions[count] == labels[count]:
        num_correct = num_correct + 1
    count = count + 1

print "the number of predictions is : "
print len(predictions)
print "the number of correct predictions is : "
print num_correct
print ""
print ((num_correct * 100) / len(predictions))

#
# for label in labels:
#     print label
# for array in word_counts:
#     print array

# dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,
#                                 filled=True, rounded=True, special_characters=True)
# graph = graphviz.Source(dot_data)

# iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)
#
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")
#
# dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,
#                                 filled=True, rounded=True, special_characters=True)
# graph = graphviz.Source(dot_data)

