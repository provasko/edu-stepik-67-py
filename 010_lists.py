students = ["Ivan", "Masha", "Sasha"]
for student in students:
    print("Hello, " + student + "!")

print(students[1])

# Access to elements

print(len(students))
print(students[:2])  # up to 2nd (number 1)
print(students[::-1])  # reverse

# Operations
teachers = ["Vova", "Alex"]
print(students + teachers)
print(teachers * 3)

# Adding elements
students.append("Seva")
students += ["Olga"]
students.insert(2, "Vsevolod")

print(students)


students = []  # empty
''' From python.org:
s[i] = x
item i of s is replaced by x
s[i:j] = t
slice of s from i to j is replaced by the contents of the iterable t
del s[i:j]
same as s[i:j] = []
s[i:j:k] = t
the elements of s[i:j:k] are replaced by those of t
(1)
del s[i:j:k]
removes the elements of s[i:j:k] from the list
s.append(x)
appends x to the end of the sequence(same as s[len(s):len(s)]=[x])
s.clear()
removes all items from s(same as del s[:])
(5)
s.copy()
creates a shallow copy of s(same as s[:])
(5)
s.extend(t) or s += t
extends s with the contents of t(for the most part the same as s[len(s):len(s)]=t)
s *= n
updates s with its contents repeated n times
(6)
s.insert(i, x)
inserts x into s at the index given by i(same as s[i:i]=[x])
s.pop() or s.pop(i)
retrieves the item at i and also removes it from s
(2)
s.remove(x)
remove the first item from s where s[i] is equal to x
(3)
s.reverse()
reverses the items of s in place
'''

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)

# Remove

students.remove("Sasha")
del students[3:-2]
print(students)

# Search

if "Ivan" in students:
    print("Got you")
if "O" not in students:
    print("O deleted successfully")

ind = students.index("Olga")

# Sorting
print(sorted(students))  # without changing
print(students)
print(students.sort())  # with changing

# Reversing
print(students.reverse())  # with changing
print(reversed(students))  # without changing
students[::-1]
