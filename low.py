import pandas as pd


def u_cal(u, n): 
    temp = u; 
    for i in range(1, n): 
        temp = temp * (u - i); 
    return temp; 
# calculating factorial of given number n 
def fact(n): 
    f = 1; 
    for i in range(2, n + 1): 
        f *= i; 
    return f;

d=[30,27,26,25,24,23,20,19,18,17,16,13]
low=[137.79,136.65,138.44,136.03,136.88,138.44,138.25,140.07,136.53,136.43,135.66,136.57]

x=list()
for i in range(0,12): 
    x.append(d[i])
 
  
# Driver Code 
  
# Number of values given 
n = 12;
# y[][] is used for difference table 
# with y[][0] used for input
y = [[0 for i in range(n)] 
        for j in range(n)]
for k in range(0,len(low)):
    y[k][0]=low[k]
'''y[0][0] = 127.79; 
y[1][0] = 136.65;
y[2][0] = 138.44;
y[3][0] = 136.03;
y[4][0] = 136.88;
y[5][0] = 138.44;
y[6][0] = 138.25;
y[7][0] = 140.07;
y[8][0] = 136.53;
y[9][0] = 136.43;
y[10][0] = 135.66;
y[11][0] = 136.57;'''

# Calculating the forward difference 
# table 
for i in range(1, n): 
    for j in range(n - i): 
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]; 
  
# Displaying the forward difference table 
for i in range(n): 
    print(x[i], end = "\t"); 
    for j in range(n - i): 
        print(y[i][j], end = "\t"); 
    print(""); 
  
# Value to interpolate at 
value =int(input("Enter the day for which you need to find LOW  :")); 
  
# initializing u and sum 
sum = y[0][0]; 
u = (value - x[0]) / (x[1] - x[0]); 
for i in range(1,n): 
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i); 
  
print("\nValue at", value,  
      "is", round(sum, 6));
    
