hi_hello='HARI'
# for i in hi_hello:
#     print(i)
    
# for i, char in enumerate(hi_hello):
#     print(i, char)
# L=len(hi_hello)
# for i,char in enumerate(hi_hello):
#     # print(i, char)
# '''HARI
#     IRAH
#     '''
str_1=''
for i in hi_hello:
    rev_name= i+str_1 #H+'' = H 
    #next loop i=A, rev_name=A+H=AH
    #next loop i=R, rev_name=R+AH=RAH
    #next loop i=I, rev_name=I+RAH=IRAH
    str_1=rev_name #H
print(str_1)

string_1='HARI'
str_2=string_1[::-1]
print(str_2)

print(string_1[0:2]) #HA #slicing method in strings HARI
print(string_1[2:]) #RI
print(string_1[:100]) #HARI
print(string_1[-2]) #R
print(string_1[-2:]) #RI