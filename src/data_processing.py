from database import Database
import matplotlib.pyplot as plt
import numpy as np
import json

with open("search_criteria.json") as file:
    candidats = json.loads(file.read())

database = Database("president")

list_candidats = []
list_count = []

for candidat in candidats:
    list_candidats.append(candidat["nom"])
    list_count.append(database.get_tweet_count(candidat["keywords"]))

"""axisx = np.array(list_pres)
axisy = np.array(list_nbtweets)"""

"""plt.bar(axisx, axisy, width = 0.1)"""

list_colors = ["#dd5c00", "#f90100", "#b901b5", "#4201b5", "#42beb5", "#6301b7", "#63014a", "#3f0121", "#03ee06",
               "#a2a6a5", "#006450", "#000001"]

plt.pie(list_count, labels=list_candidats, colors=list_colors)

plt.show()
date = []
for i in range(11, 21):
    date.append("2022-03-" + str(i))


for d in date:
    for candidat in candidats:
        count = database.get_tweet_count(candidat["keywords"], d)
        try:
            candidat["count"].append(count)
        except KeyError:
            candidat["count"] = [count]

for candidat in candidats:
    plt.plot(date, candidat["count"])

plt.legend(list_candidats)
plt.show()
git@github.com:PhoqueEberlue/leboncoin-scrapper.git