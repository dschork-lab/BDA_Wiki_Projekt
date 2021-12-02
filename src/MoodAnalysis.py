import csv
import numpy as np

reducedCsv = []
wordOnlyCsv = []

# Single execution on import
# Reads the english only csv mood lexicon file and remove entries without any value
with open('./../NRC-Emotion-Lexicon-English-only.csv') as moodAnalysisCsv:
    csvReader = csv.reader(moodAnalysisCsv, delimiter=';')
    for row in csvReader:
        if True in [row[x] == '1' for x in range(1, 11)]:
            reducedCsv.append(row)
            wordOnlyCsv.append(row[0])


# Takes an full wikipedia article and calculate the mood values
# Meaning of the values in the Numpy Array
# 0: Positive
# 1: Negative
# 2: Anger
# 3: Anticipation
# 4: Disgust
# 5: Fear
# 6: Joy
# 7: Sadness
# 8: Surprise
# 9: Trust
def check_mood(article: str) -> np.ndarray:
    article_list = np.array(article.split())
    article_counter = dict(zip(*np.unique(article_list, return_counts=True)))
    article_result = np.zeros(10)

    for index, term in enumerate(wordOnlyCsv):
        if term in article_list:
            for i in range(10):
                article_result[i] += int(reducedCsv[index][i + 1]) * article_counter[term]

    return article_result
