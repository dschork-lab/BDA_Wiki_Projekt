import csv
from typing import Union, Any

reducedCsv = []

# Single execution on import
# Reads the english only csv mood lexicon file and remove entries without any value
with open('./../NRC-Emotion-Lexicon-English-only.csv') as moodAnalysisCsv:
    csvReader = csv.reader(moodAnalysisCsv, delimiter=';')
    for row in csvReader:
        if row[1] == '1' or row[2] == '1' or row[3] == '1' or row[4] == '1' or row[5] == '1' or row[6] == '1' or row[7] == '1' or row[8] == '1' or row[9] == '1' or row[10] == '1':
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
def check_mood(article: str) -> list[Union[int, Any]]:
    article_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    article_list = article.split()
    for word in article_list:
        word_result = check_mood_for_word(word)
        for i, result in enumerate(word_result):
            article_result[i] = article_result[i] + result
    return article_result


# Mood analysis for a single word (Tuple description see check_mood())
def check_mood_for_word(word: str) -> tuple[int, int, int, int, int, int, int, int, int, int]:
    for row in reducedCsv:
        if row[0].lower() == word.lower():
            return (
                int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]),
                int(row[9]), int(row[10]))
    return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0