elye = []
temp = []

with open('day-1.txt') as f:
    text = f.read()
    t = text.split('\n')
    for i in t:
        if i == '':
            elye.append(temp)
            temp = []
        else:
            temp.append(int(i))

elye.append(temp)

s = [sum(i) for i in elye]

# sum of top three in s
s = sorted(s, reverse=True)
print(s)
print(sum(s[:3]))

# Solving puzzles with programming is fun! I'm a beginner in Python and I'm learning it by solving puzzles. I'm also learning how to use git and github. I'm a beginner in Python and I'm learning it by solving puzzles. I'm also learning how to use git and github.
# 