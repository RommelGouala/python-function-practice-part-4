# Write a Python function called max_num()to find the maximum of three numbers.


def max_num(x, y, z):
    return max([x, y, z])

print(max_num(1, 2, 3))
print(max_num(50, 75, 1225))


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i 
    return prod

print(mult_list([2,2,3]))
print(mult_list([]))
print(mult_list([25]))


# Write a Python function called rev_string() to reverse a string.
def Rv_string(string):
    return string[::-1]

print(Rv_string("hello"))
print(Rv_string("Love"))
print(Rv_string("we are not going to fail"))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(start, stop, step):
    return start in range(stop, step+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(24,15,17))





# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(names):
    return print("No problemo", names)

pascal("pascal")