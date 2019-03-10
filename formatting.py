name = "Joe"
age = 65
career = "Doctor"

result = "Hi, my name is " + name + ", and my age is " + age + ", and my career is " + career + "."
result2 = "Hi, my name is %s, and my age is %d, and my career is %s." % name, age, career
result3 = "Hi, my name is {}, and my age is {}, and my career is {}.".format(name, age, career)
result4 = f"Hi, my name is {name}, and my age is {age}, and my career is {career}."     #good and intuitive option over the previous


print(result)
print(result2)
print(result3)
print(result4)
