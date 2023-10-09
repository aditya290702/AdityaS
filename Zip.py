#when we have tyo operate on multiple list
days = ['monday','tuesday','wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','milk']
desserts = ['chocolava','ice cream','cake',]

for days,fruits,drinks,desserts in zip(days, fruits, drinks, desserts):
    print(days, ":drink", drinks, "-eat:",fruits, "and enjoy" ,desserts)