import csv
from typing import List

reducedCsv = []

# Single execution on import
# Reads the english only csv mood lexicon file and remove entries without any value
with open('./../NRC-Emotion-Lexicon-English-only.csv') as moodAnalysisCsv:
    csvReader = csv.reader(moodAnalysisCsv, delimiter=';')
    for row in csvReader:
        if True in [row[x] == '1' for x in range(1, 11)]:
            reducedCsv.append(row)


# Takes an full wikipedia article and calculate the mood values
# Meaning of the values in the tuple
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
def check_mood(article: str) -> List[int]:
    article_result = [0 for _ in range(10)]
    article_list = article.split()
    for word in article_list:
        word_result = check_mood_for_word(word)
        for i, result in enumerate(word_result):
            article_result[i] = article_result[i] + result
    return article_result


# Mood analysis for a single word (Tuple description see check_mood())
def check_mood_for_word(word: str) -> List[int]:
    for row in reducedCsv:
        if row[0].lower() == word.lower():
            return [int(row[x]) for x in range(1, 11)]
    return [0 for _ in range(10)]
