# Calculate income tax for the given income by adhering to the below rules

total_income=45000
your_tex = 0
if (total_income <=10000):
    print("no pay for tex")

elif(total_income <=20000):
    x = total_income - 10000 

    your_tex=x * 10/100
    print(your_tex)

else:
    your_tex=10000 * 10 / 100

    your_tex = your_tex + (total_income - 20000) * 20 / 100

    print(your_tex)


