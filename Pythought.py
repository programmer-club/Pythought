import random
def validate(prmt, optn, msg):
  msgon = True
  while not text in optn:
    text = input(prmt)
    if msgon == False:
      print(msg)
    msgon = False
  return text
def value(values):
    while not random in values:
        random = random.randint(1, )
    if random == 1:
        value = varse[random.randint(1, len(varse))]
    if random == 2:
        value = strings[random.randint(1, len(strings))]
    if random == 3:
        value = nums[random.randint(1, len(nums))]
    if random == 4:
        value = bools[random.randint(1, len(bools))]
    if random == 5:
        value = simpbools[random.randint(1, len(simpbools))]
    if random == 6:
        value = origfuncs[random.randint(1, len(origfuncs))]
    if random == 7:
        value = funcs[random.randint(1, len(funcs))]
pipon = validate("Would you like to import a pip module? y/n/Y/N", ("y", "n", "Y", "N"), "Please use a valid input.")
varse[""]
strings[""]
nums[""]
bools["True", "False", "None"]
simpbools["True", "False"]
origfuncs[""]
funcs[""]
abclen = 1
abcnum = 0
abc = "abcdefghijklmnopqrstuvwxyz"
def var():
  if abcnum == 26:
    abclen =+ 1
  abcnum =+ 1
  X = abclen - 1
  while not X == 0:
    var_name =+ "X"
  var_name =+ abc[abcnum]
