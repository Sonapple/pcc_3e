names = ['Mom','John','Mike','Jessy'] #Count: 0,1,2,3 
date = "Sep,20.2025"
for name in names:
    print(f"Hello {name.title()}, Your are invite to dinner on {date}")
#Mike cant make it
MikeOut = names.pop(2)
print(f"{MikeOut} cant make it")
names.append("Mark")
for name in names:
    print(f"Hello {name}, Your are invite to dinner on {date}")
length = len(names)
print(length)
