from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

#slices = [120, 80, 30, 20]
#labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
#colors = ['blue', 'red', 'yellow', 'green']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
explode = [0, 0, 0, 0.1, 0]

#plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})
plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
