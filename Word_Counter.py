
with open("word_list.txt") as f:
  hist = f.readlines()
def slash_n_remover(name):
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