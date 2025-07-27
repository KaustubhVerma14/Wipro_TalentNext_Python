# PROJECT-1 

a=int(input("How far do you want to travel?(in miles) - "))
if a<=3:
    print("I suggest you travel through a Bicycle")
elif a>3 and a<300:
    print("I suggest you travel through a Motor-cycle")
elif a>=300:
    print("I suggest you travel through a Super-Car")
else:
    print("Invalid Input")


# PROJECT-2

cost_per_hr=0.51
cost_per_day=24*cost_per_hr
cost_per_week=7*cost_per_day
cost_per_month=30*cost_per_day
print("Cost to operate per day",cost_per_day)
print("Cost to operate per week",cost_per_week)
print("Cost to operate per month",cost_per_month)
money=918
days_charge_lasts=money/cost_per_day
print("$918 will last",days_charge_lasts,"days")