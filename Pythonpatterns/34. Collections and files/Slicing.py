# String slicing
text = "Learn Python"
# first 3 characters
print(text[:3])
#first four (0-4)
print(text[:4])  #Lear
# last 4
print(text[-4:]) #thon
#9 to end
print(text[9:]) #hon
ln= len(text)
print(text[ln-6:ln+1]) #Python

#using stride
print(text[:6:1])
print(text[:6:2])

# reverse a string
name = "I love Python"
newname = name[-1::-1]  # nohtyP evol I

