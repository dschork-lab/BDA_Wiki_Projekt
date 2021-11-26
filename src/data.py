import matplotlib.pyplot as plt
import numpy as np
import pymongo
import pandas as pd


def get_mood_data():
    # connect to MongoDB
    client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')
    # get database 'article_information'
    article_information_db = client['article_information']
    # get mood collection
    mood_collection = article_information_db['id_mood']
    return pd.DataFrame(list(mood_collection.find()))


def round_float_list(values, digits):
    rounded = []

    for item in values:
        rounded.append(round(item, digits))

    return rounded


def plot_average_data(data):
    labels = ['positive', 'negative', 'anger', 'anticipation', 'disgust', 'fear', 'joy',
              'sadness', 'surprise', 'trust']

    old_means = [data['old_positive'].mean(), data['old_negative'].mean(), data['old_anger'].mean(),
                 data['old_anticipation'].mean(), data['old_disgust'].mean(), data['old_fear'].mean(),
                 data['old_joy'].mean(), data['old_sadness'].mean(), data['old_surprise'].mean(),
                 data['old_trust'].mean()]
    new_means = [data['new_positive'].mean(), data['new_negative'].mean(), data['new_anger'].mean(),
                 data['new_anticipation'].mean(), data['new_disgust'].mean(), data['new_fear'].mean(),
                 data['new_joy'].mean(), data['new_sadness'].mean(), data['new_surprise'].mean(),
                 data['new_trust'].mean()]

    old_means = round_float_list(old_means, 1)
    new_means = round_float_list(new_means, 1)

    x = np.arange(len(labels))  # label locations
    width = 0.45  # width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, old_means, width, label='Old', color=(0.07, 0.17, 0.56))
    rects2 = ax.bar(x + width / 2, new_means, width, label='New', color=(0.16, 0.5, 0.17))

    # add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Comparison of article mood before and after the last edit')
    ax.set_xticks(x, labels, rotation='vertical')
    ax.legend()

    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)

    fig.set_figwidth(10)
    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    mood_data = get_mood_data()
    plot_average_data(mood_data)