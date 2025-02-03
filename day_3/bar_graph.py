import matplotlib.pyplot as plt

fruits =["apple","banana","orange","grapes","mango"]
quantity=[10,20,30,40,50]
plt.bar(fruits,quantity,color=['red','blue','green','orange','yellow'])
plt.title("Fruits vs Quantity")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()