# 1
# def calculate_years(principal, interest, tax, desired):
#     years = 0
#     while desired > principal:
#         principal += (principal*interest)*(1-tax)
#         years += 1
#     return print(years)

# calculate_years(1000.00,0.05,0.18,1100.00)
# calculate_years(1200.00,0.17,0.06,2000.00)
# calculate_years(1500.00,0.07,0.6,5000.00)



#2 
# def expandedForm(num):
#     a = str(num)
#     z = ''

#     for loop in range (len(a)):
#         if a[loop] != '0':
#             if loop == len(a)-1:
#                 z+= str(int(a[loop]) * 10**(len(a)-1-loop))
#             else:
#                 z+= str(int(a[loop]) * 10**(len(a)-1-loop)) + ' + ' 
#     return print(z)

# expandedForm(12)
# expandedForm(42)
# expandedForm(7048)



#3
def tower_builder (n_floor, block_size):
    a = 0
    b = []
    c = 0
    w, h = block_size
    z = ''
    for loop1 in range (n_floor):
        for loop2 in range(h):
            for loop3 in range (((n_floor-1)*w)-(loop1*w)):
                z += '-'
            for loop4 in range (w+(loop1*(w*2))):
                a += 1
                b.append(a)
                z += str(b[c])
                c += 1
            z += '\n'
    return print(z)

tower_builder(3,(2,3))
# tower_builder(6,(2,1))
# tower_builder(4,(4,3))