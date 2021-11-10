print("Car Stats Input:")
racetype = input("    enter race type: ").strip().lower()
racetypes = ["drag", "road", "street", "rally", "freeroam", "drift"]
if not racetype in racetypes:
    print("    You must enter a valid race type.")
    print("    Current availible race types are ", end="")
    print(racetypes)
    exit(1)
weight = float(input("    enter car weight: "))
power = float(input("    enter car horsepower: "))
drive = input("    enter car's drive type: ").strip().lower()
frontweight = float(input("    enter car's front weight value (as a decimal): "))

#Tire pressure
print("\nTire pressure settings:")
if racetype == "drag":
    if drive == "fwd":
        print("    front tire pressure: minimum availible")
        print("    rear tire pressure: max availible")
    elif drive == "rwd":
        print("    front tire pressure: max availible")
        print("    rear tire pressure: minimum availible")
    elif drive == "awd":
        print("    front tire pressure: minimum availible")
        print("    rear tire pressure: minimum availible")
    else:
        print("    invalid drive type: " + str(drive))
        exit(1)
elif racetype == "road":
    print("    Tire pressure for road racing is best tuned on track")
    print("    Keep it around 30 psi and tune such that it sits at around 33 psi after use")
elif racetype == "street":
    pass
elif racetype == "rally":
    print("    Rally pressure is best tuned on track")
    print("    lower pressure is more forgiving, but will cause more mistakes")
    print("    higher pressure is less forgiving, but will cause less mistakes")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Gearing
print("\nGearing Settings:")
if racetype == "drag":
    print("    gearing should be tuned on track")
elif racetype == "road":
    pass
elif racetype == "street":
    pass
elif racetype == "rally":
    pass
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Alignment
print("\nAlignment Settings:")
if racetype == "drag":
    pass
elif racetype == "road":
    print("    front and rear camber outside should be tuned to be barely positive while turning")
    print("    set toe to 0 to start, but this should then be tuned on track")
    print("    set to around 6.5")
elif racetype == "street":
    pass
elif racetype == "rally":
    print("    front and rear camber outside should be tuned to be barely positive while turning")
    print("    small amounts (0.1-0.5) of front toe out and rear toe in can be good in rally")
    print("    set somewhere between 4 and 6")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Roll Bars
print("\nRoll Bar Settings:")
if racetype == "drag":
    print("    front roll bars: minimum availible")
    print("    rear roll bars: minimum availible")
elif racetype == "road":
    rollbarMax = float(input("    Enter maximum roll bar setting: "))
    rollbarMin = float(input("    Enter minimum roll bar setting: "))
    frontRollBar = ((rollbarMax-rollbarMin)*frontweight)+rollbarMin
    rearRollBar = ((rollbarMax-rollbarMin)*(1-frontweight))+rollbarMin
    print("    front roll bar: " + str(frontRollBar))
    print("    rear roll bar: " + str(rearRollBar))
elif racetype == "street":
    pass
elif racetype == "rally":
    rollbarMax = float(input("    Enter maximum roll bar setting: "))
    print("    front roll bar: " + str(rollbarMax*0.2))
    print("    rear roll bar: " + str(rollbarMax*0.2))
    print("    roll bars should be modified based on driving conditions, use lower for worse conditions and higher for better.")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Springs
print("\nSpring Settings:")
if racetype == "drag":
    pass
elif racetype == "road":
    springMax = float(input("    enter maximum spring setting: "))
    springMin = float(input("    enter minimum spring setting: "))
    frontSpring = ((springMax-springMin)*frontweight)+springMin
    rearSpring = ((springMax-springMin)*(1-frontweight))+springMin
    print("    front spring: " + str(frontSpring))
    print("    rear spring: " + str(rearSpring))
    print("    ride height should be tuned on track")
    print("    try to make it as low as possible without bottoming out")
    print("    the stock values are usually a good starting point")
elif racetype == "street":
    pass
elif racetype == "rally":
    springMax = float(input("    enter maximum spring setting: "))
    springMin = float(input("    enter minimum spring setting: "))
    frontSpring = ((springMax-springMin)*frontweight)+springMin
    rearSpring = ((springMax-springMin)*(1-frontweight))+springMin
    print("    front spring: " + str(frontSpring))
    print("    rear spring: " + str(rearSpring))
    print("    ride height should be tuned on track")
    print("    try to make it as low as possible without bottoming out")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Damping 
print("\nDamping Settings:")
if racetype == "drag":
    pass
elif racetype == "road":
    reboundMax = float(input("    enter maximum rebound stiffness: "))
    reboundMin = float(input("    enter minimum rebound stiffness: "))
    frontRebound = ((reboundMax-reboundMin)*frontweight)+reboundMin
    rearRebound = ((reboundMax-reboundMin)*(1-frontweight))+reboundMin
    print("    front rebound: " + str(frontRebound))
    print("    rear rebound: " + str(rearRebound))

    print("    front bump Stiffness: " + str(frontRebound*0.6))
    print("    rear bump Stiffness: " + str(rearRebound*0.6))
elif racetype == "street":
    pass
elif racetype == "rally":
    reboundMax = float(input("    enter maximum rebound stiffness: "))
    reboundMin = float(input("    enter minimum rebound stiffness: "))
    frontRebound = ((reboundMax-reboundMin)*frontweight)+reboundMin
    rearRebound = ((reboundMax-reboundMin)*(1-frontweight))+reboundMin
    print("    front rebound: " + str(frontRebound))
    print("    rear rebound: " + str(rearRebound))

    print("    front bump Stiffness: " + str(frontRebound*0.6))
    print("    rear bump Stiffness: " + str(rearRebound*0.6))
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Aero
print("\nAero Settings:")
if racetype == "drag":
    print("    You probably shouldn't have aero on a drag build")
    print("    But if you do, set all of it to as low as possible")
elif racetype == "road":
    print("    Set rear wing and front splitter as high as possible")
elif racetype == "street":
    pass
elif racetype == "rally":
    print("    rally typically doesn't hit high enough speeds for aero to be effective")
    print("    But if you have it, set it as high as possible")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Brake
print("\nBrake Settings:")
if racetype == "drag":
    print("    brake tuning is completely useless in drag, up to personal preference")
elif racetype == "road":
    pass
elif racetype == "street":
    pass
elif racetype == "rally":
    print("    move breaking balance towards rear to prevent forward roll while breaking.")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass

#Differential
print("\nDiff Settings:")
if racetype == "drag":
    print("    Set acceleration to 100 wherever availible")
    if drive == "awd":
        print("    Diff balance needs to be tuned on track, keep it within 20 percent + or - from the middle")
elif racetype == "road":
    pass
elif racetype == "street":
    pass
elif racetype == "rally":
    print("    typically a lower (<50%) front diff lock and a higher (>50%) rear diff is good for rally.")
    print("    rear diff lock and balance can be used to fine tune oversteer")
elif racetype == "freeroam":
    pass
elif racetype == "drift":
    pass
