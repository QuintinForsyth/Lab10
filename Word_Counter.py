# word list can be edited for further use. i could add code to ignore capitals but i decided the same word is different
with open("word_list.txt") as f:
  hist = f.readlines()
def slash_n_remover(name):
  '''
  gets rid of /n
  '''
  fixed_name = name[0:len(name)-1]
  return (fixed_name)
histogram={}
new_name = ""
for name in hist:
  if name in histogram:
    new_name = slash_n_remover(name)
    histogram[new_name] += 1
  else:
    new_name = slash_n_remover(name)
    histogram[new_name] = 1
print(histogram)