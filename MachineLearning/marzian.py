file = open("marziani.csv").readlines()
marz_dict = {}
labels = []

for label in file[0].split(","):
    marz_dict[label] = []
    labels.append(label)

for row in file[1:]:
    for i, campo in enumerate(row.split(",")):
        if not campo in marz_dict[labels[i]] and campo != " " and campo != "" and campo != "\n":
            marz_dict[labels[i]] = marz_dict[labels[i]] + [campo]

print(marz_dict)
