# Scenario
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.



co=int(input())
i=0
while co != 1 :
    if co % 2 ==0:
        co=co/2
    else:
        co=(3*co+1)
    print(int(co))
    i+=1
print("Steps =",i)