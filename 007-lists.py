'''
array, feld, 

list
'''

def get_add_elements2fibonaci(fib_number_list, number_of_elements2add = 1):
    fib = fib_number_list[-2:] 
    for i in range(number_of_elements2add):
        fib.append(fib[-1] + fib[-2])
    return fib[2:]  
   
fib = [1,
       1,
       2,
       3,
       5,
       8,
       13,       
       ]
       
print(fib)
for i, element in enumerate(fib):
    print(i, element)

a = 2
'''
for i in get_add_elements2fibonaci(
             fib_number_list = fib, 
             number_of_elements2add = 3):
    fib.append(i)                
'''
fib.extend(get_add_elements2fibonaci( 
             fib_number_list = fib, 
             number_of_elements2add = 3
           ))

print(fib)






