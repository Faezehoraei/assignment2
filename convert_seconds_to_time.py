# In The Name Of GOD
# Programmer is : Faezeh Oraei MiriNejad
# ID is : 96440164

print("please enter the seconds:")
inp = int(input('seconds = '))
hour = inp // 3600
minute = (inp - 3600 * hour) // 60
second = (inp - 3600 * hour) - 60 * minute
print("Convert seconds to time = ", hour,':', minute,':', second )