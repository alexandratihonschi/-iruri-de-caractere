s=str(input('introduceti sirul: '))
i=0
z=0
i+=s.count('A')
print('litera A apare in sir de:',i,'ori')
x=s.replace('B',' ')
print('sirul obtinut dupa redierea literet B:',x)
z+=s.count('MA')
print('silaba MA apare in sirul',s,'de',z,'ori')
v=s.replace('MA','TA')
print('sirul obtinut prin inlocuirea silabei MA prin TA:',v)
qw=s.replace('TO',' ')
print('sirul obtinut dupa redierea silabei TO:',qw)
print('\nScrierea inversa a sirului introdus de la tastatura:')
for i in reversed(range(0, len(s))):
    print(s[i], end=" ")