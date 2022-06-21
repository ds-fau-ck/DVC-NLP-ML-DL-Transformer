from sklearn.feature_extraction.text import CountVectorizer

corpus=[
    "zebra apple ball cat",
    "ball cat dog elephant",
    "very very unique"
]
Vectorizer=CountVectorizer()
X=Vectorizer.fit_transform(corpus)
print(X.toarray())
print(Vectorizer.get_feature_names_out())