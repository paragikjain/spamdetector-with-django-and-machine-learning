# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:23:43 2019

@author: Parag_IK
"""
def machine(stringx):
    import pandas as pd
    import numpy as np
    from django.conf import settings
    import re
    from nltk.stem.porter import PorterStemmer
    from nltk.corpus import stopwords

    data = pd.read_csv(settings.DATA_DIR+'/spam.csv', encoding='latin-1')
    data = data.iloc[:, [0, 1]]
    data['v1'] = data.v1.map({'ham': 0, 'spam': 1})

    courpas = []
    # data_cleaning
    string = stringx
    df2 = pd.DataFrame({"v1": [0],
                        "v2": [string]})
    data = data.append(df2, ignore_index=True)

    # data_cleaning
    for a in data['v2']:
        review = re.sub('[^a-zA-Z]', ' ', a)
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(x) for x in review if not x in stopwords.words('english')]
        review = ' '.join(review)
        courpas.append(review)

    # create a bag of word model
    from sklearn.feature_extraction.text import CountVectorizer

    cv = CountVectorizer(max_features=5000)
    x = cv.fit_transform(courpas).toarray()
    y = data.iloc[:, 0].values
    x_train, ytrain = x[:-1], y[:-1]
    x_test, y_test = x[5572:5573], y[5572:5573]
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB

    classifier = GaussianNB()
    classifier.fit(x_train, ytrain)
    y_pred = classifier.predict(x_test)

    if y_pred == 1:
        return 'spam'

    else:
        return 'ham'



