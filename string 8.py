name = "Sam"
friend ='sana'
print("hello ," + name)

#"" ke ander ek aur "" nhi dal skte h  to  hm slicing kr skte h aur string ko single quote me kr skte h n triple single quote, triple double quotes me kuch bhi likho wo string ban jati h
# apple = "He said,"I want to eat an apple"

apple = "He said ,\"I want to eat an apple"
print(apple)
apple='He said,"I want to eat an apple'
print(apple)
apple ='''He said,
Hi Sam 
hey i am good
"I want to eat an apple'''
print(apple)
#INDEXING
print(name[0])
print(name[2])
print(name[1])

#For loop - for multi paragraph

print("Lets use a for loop \n")
for character in apple:
    print(character)