You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00

Program:

prin,inter,time_va = list(input().split())
a = int(prin)
b = float(inter)
c = int(time_va)
S_I = (a*b*c)/100
val = round(S_I,2) # round() is used to roundoff the values, and round(given_values,number_after_decimal_need)
print(val)
