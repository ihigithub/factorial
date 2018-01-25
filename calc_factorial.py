# this script calculates the factorial of a given number

def calc_fact(item):
    if isinstance(item, int) == True:
        product = 1
        while item > 0:
            product *= item
            item=item-1
        return product
    else:
        print "instance is not an integer"

def calc_fact_recursive(item):
    if isinstance(item, int) == True:
        return item * calc_fact(item-1)
    else:
        print "instance is not an integer"




# test calculation

print calc_fact(6)
print calc_fact_recursive(6)