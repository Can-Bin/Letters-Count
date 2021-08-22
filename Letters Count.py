Letters Count
sentence = input("Please write a sentence : ")
empty_dict = {}
for i in set(sentence):
  empty_dict[i]=sentence.count(i)
print(empty_dict)