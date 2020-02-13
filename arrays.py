"""python collection ( arrays)"""
#list ordered and changeable/mutable
students=["mercy","john","alex","abdi"]
print(students)
#indexing from right to left starts from 0 while indexing from left to right starts from -1
#it outputs the first list mercy
print("students[0]  : ", students[0])
#it  outputs the abdi
print("students[-1]:",students[-1])
#it outputs the first and the second list john and alex
print("students[1:3]:",students[1:3])
#it outputs the first three list mercy ,john and alex
print("students[-4:-1]:",students[-4:-1])
#it outputs the first three lists mercy ,hohn and alex
print("students[:3]:",students[:3])
#change items in a list
students[2]="kamau"
print(students)
students[-4:-3]="chela","silah"
print(students)
#loop through list
for a in students:
    print(a)
    #check if item exists

    if "chela"in students :
        print("present")
    else:
        print("absent")
    if "chela" not in students:
        print("absent")
    else:
        print("present")

    #list methods
    #len
students=["mercy","john","alex","abdi"]
#it outputs four items
print(len(students))
#apend
students.append("noor")
#append adds noor at the end
print(students)
#it has inserted kamau at index 2
students.insert(2,"kamau")
print(students)
#index
#it returns the position  at the first occurence of the specified value
people=['silantoi','lenkai','sanaipei']
y=people.index("sanaipei")
print(y)
#remove
#removes the first item from the specified value
animals=['lion','cheetah','leopard']
animals.remove("lion")
print(animals)
#clear removes all the elements from the list
subjects=['english','kiswahili','maths']
subjects.clear()
print(subjects)
#copy returns a copy of the list
units=['python','database','computer applications']
y=units.copy()
print(units)
#sort sorts the list ascending by default
cities=['nairobi','kisumu','mombasa']
cities.sort()
print(cities)
#reverse -reverses the order of the list
clothes=['dresses','trousers','shorts']
clothes.reverse()
print( clothes)

#join 2 lists
a=['a','b','c']
b=[1,2,3]
list=a+b
#it joins the two lists into one
print(list)







