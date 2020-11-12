age = 23
name = "Rajesh Kumat"
city = "Bharatpur"

txt = "his name is {1}. {1} is {0} years old. {1} is from {2}"
print(txt.format(age,name,city))
#named indexes
order = "i have a  {bikename} bike. It is a {model}"
print(order.format(bikename="pulser", model=220))
