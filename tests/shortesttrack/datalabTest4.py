from datalab.storage._item import Item

item = Item(key = "MLP_TRAIN.tar.gz")
content = item.read_from()
print (content)

with open("MLP_TRAIN.tar.gz", 'wb') as f:
    f.write(content)

