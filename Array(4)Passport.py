You are a passport issuer, but due to some problems in the system, 
there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers. You are given a list of passport numbers.

Input Description:
You are given length of list.Second line,You are given with a list.

Output Description:
Print the list of passport numbers without duplicates.
Sample Input :
5
A23 B56 B56 C79 D16
Sample Output :
A23 B56 C79 D16

Program:
def Remove_duplicate(passport_number):
    l = []
    for i in passport_number:
        if i not in l:
            l.append(i)
    print(*l)

if __name__ == '__main__':
    number = int(input())
    passport_number = input().split()
    Remove_duplicate(passport_number)
                                                  or
def Remove_Duplicate(val):
  soted = list(dict.fromkeys(val))
  for i in soted:
    sum = i.rstrip()
    print(sum,end=" ")
if __name__== '__main__':
    values = int(input())
    val = list(map(str,input().split()))
    Remove_Duplicate(val)
