from math import log
from typing import List


class CountVectorizer:

    def __init__(self):
        self._vocabulary = []
        self._matrix = []

    def fit_transform(self, corpus: list[str]) -> list:
        assert isinstance(corpus, list), 'corpus is not list'
        split_corpus = []
        count_words = 0
        for line in corpus:
            split_line = line.lower().split()
            split_corpus.append(split_line)
            for el in split_line:
                if el not in self._vocabulary:
                    self._vocabulary.append(el)

        for i in range(len(split_corpus)):
            self._matrix.append([])
            for el in self._vocabulary:
                word_counter = 0
                for word in split_corpus[i]:
                    if word == el:
                        word_counter += 1
                self._matrix[i].append(word_counter)

        return self._matrix

    def get_feature_names(self) -> list:

        return self._vocabulary


class TfidfTransformer():


    def idf_transform(self, matr: List[List[int]]) -> List[float]:
        colm_len = len(matr[0])
        len_matr = len(matr)
        idf = []
        for word_index in range(colm_len):
            counter = 0
            for doc in matr:
                if doc[word_index] != 0:
                    counter += 1
            idf.append(log((len_matr + 1) / (counter + 1)) + 1)

        return idf

    def tf_transform(self, matr: list[list[int]]) -> list[list[float]]:
        sum_word = 0
        freq_list = []
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number / sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list


    def fit_transform(self, matr:List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(matr)
        idf = self.idf_transform(matr)

        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]

        tf_sum = [sum(row) for row in list(zip(*tf))]
        tf_idf = [x * y for x, y in zip(tf_sum, idf)]

        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        self.transformer = TfidfTransformer# композиция классов , предпочтительнее
        super().__init__() #чтобы вызывать родительский класс
        self.foo = []


    def fit_transform(self, corpus: list[str]) -> list:
        matrica = super().fit_transform(matr) #получаем объект родительского класса
        self.transformer.fit_transform()
        return self.transformer.fit_transform(matr)


class TfidVectorizerV2:
    def __init__(self, ):
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()


    def fit_transform(self, corpus: list[str]) -> list:
        matrica = self.vectorizer.fit_transform(matr)#получаем объект родительского класса
        self.transformer.fit_transform()
        return self.transformer.fit_transform(matrica)


    def get_feature_names(self):
        return self.vectorizer.get_feature_names()


def check() -> None:
    SOURCE_FILE_NAME = 'Pasta.txt'
    vec = CountVectorizer()
    corpus = []
    with open(SOURCE_FILE_NAME, encoding="utf8") as file:
        for line in file.readlines():
            corpus.append(line)

    print(vec.fit_transform(corpus))
    print(vec.get_feature_names())




##1
count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

def tf_transform(matr : list[list[int]]) -> list[list[float]]:
    sum_word = 0
    freq_list = []
    for one_list in matr:
        sum_word = sum(one_list)
        sentence_tf = []
        for number in one_list:
            freq = number/sum_word
            sentence_tf.append(freq)
        freq_list.append(sentence_tf)
    return freq_list

if __name__=='__main__':
    matr = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(tf_transform(matr))

##2
count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

def idf_transform(matr : List[List[int]]) -> List[float]:
    colm_len = len(matr[0])
    len_matr = len(matr)
    idf = []
    for word_index in range(colm_len):
        counter = 0
        for doc in matr:
            if doc[word_index] != 0:
              counter += 1
        idf.append(log((len_matr + 1)/(counter + 1)) + 1)
    return idf
##2 (2)
# count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
# 'abc'
# 'abc'
# #zip get us получаем кортеж , транспонирование матрицы
# zip('123','abc')
matr1 = [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0]
def count_pos(matrix: List[int] -> int):
    counter = 0
    for el in matrix:
        if el > 0:
            counter += 1
    return counter
##
abc = [i>0 for i in [1,2,3,0]]
print(sum(abc))
##
matrix = [1, 1, 2, 1, 1, 1, -1, 0, 0, 0, 0, 0]
positive_numbers = list(filter(bool, matrix))
print(positive_numbers)
##
matrix = [1, 1, 2, 1, 1, 1, -1, 0, 0, 0, 0, 0]
positive_numbers = list(filter(lambda x: x > 0 , matrix))
print(positive_numbers)
##
from typing import List
class TfidfTransformer():


    def idf_transform(self, matr: List[List[int]]) -> List[float]:
        colm_len = len(matr[0])
        len_matr = len(matr)
        idf = []
        for word_index in range(colm_len):
            counter = 0
            for doc in matr:
                if doc[word_index] != 0:
                    counter += 1
            idf.append(log((len_matr + 1) / (counter + 1)) + 1)

        return idf

    def tf_transform(self, matr: list[list[int]]) -> list[list[float]]:
        sum_word = 0
        freq_list = []
        for one_list in matr:
            sum_word = sum(one_list)
            sentence_tf = []
            for number in one_list:
                freq = number / sum_word
                sentence_tf.append(freq)
            freq_list.append(sentence_tf)
        return freq_list


    def fit_transform(self, matr:List[List[int]]) -> List[List[float]]:
        tf = self.tf_transform(matr)
        idf = self.idf_transform(matr)

        tf_idf = [[x * y for x, y in zip(row, idf)] for row in tf]

        tf_sum = [sum(row) for row in matr in list(zip(*tf))]
        tf_idf = [x * y for x, y in zip(tf_sum, idf)]

        return tf_idf

    # answer[[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],[0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
##





