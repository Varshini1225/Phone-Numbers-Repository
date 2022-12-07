repository={9502570720:'Shaheen',9381942115:'Kalyan',9676678735:'Varshini',8125143865:'Tarun',9032420995:'Maviya',9798434389:'Prachi',9718845025:'Dhruv'}
c=list(repository.keys())
c1=[]
for i in repository:
    c1.append(repository[i])
repository1=dict(zip(c1,c))

name=input('Enter name: ')
def call3(name):
    print(repository1[name])
call3(name)

n=int(input('Enter contact number:'))
def call2(n):
    print(repository[n])
call2(n)

def call1(n1=len(c)):
    print('contact\t\tname')
    for j in range(n1):
        print(c[j],'\t\t',repository[c[j]])
a=input('Enter True if you want to extract whole data of repository:')
if a=='True':
    call1()
a1=input('Enter True if you want to extract no of data:')
if a1=='True':
    n1=int(input('Enter number of contact:'))
    call1(n1)
