filename = 'demo_open.txt'

with open(filename, 'w') as f:

    f.write('ID,var1,var2,var3\n')

    f.write('1001,5,1.23,"Y"\n')
    f.write('1002,5,1.33,"N"\n')
    f.write('1003,6,1.28,"Y"\n')
    f.write('1004,5,1.24,"Y"\n')

