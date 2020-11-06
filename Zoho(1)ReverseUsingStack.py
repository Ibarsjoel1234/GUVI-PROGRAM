You are provided with a string ‘s’. Your task is to reverse the string using stack Data Structure.



def reverse(s):
    a = []
    l = []
    for word in s:
        a.append(word)
    for words in range(len(a)):
        l.append(a.pop())
    print(" ".join(l))

if __name__ == '__main__':
    s = input().split()
    reverse(s)
