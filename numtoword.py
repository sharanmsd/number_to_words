# Numbers to words
n=int(input())
unitdigit=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tensdigit=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
hundredsdigit=[' ','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
thousdigit=['','one thousand','two thousand','three thousand','four thousand','five thousand','six thousand','seven thousand','eight thousand','nine thousand']
if(n<20):
    print(unitdigit[n])
elif(n<100):
    a=n%10
    b=n//10
    ds=''
    ds=tensdigit[b]+' '+unitdigit[a]
    print(ds)
elif(n<1000):
    a=(n//100)%10
    b=(n//10)%10
    c=n%10
    ds=''
    ds=hundredsdigit[a]+' and '+tensdigit[b]+' '+unitdigit[c]
    print(ds)
elif(n<10000):
    a=(n//1000)%10
    b=(n//100)%10
    c=(n//10)%10
    d=n%10
    ds=''
    ds=thousdigit[a]+' '+hundredsdigit[b]+' and '+tensdigit[c]+' '+unitdigit[d]
    print(ds)
