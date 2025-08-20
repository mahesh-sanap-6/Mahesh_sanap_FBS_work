# Convert distant given in feet and inches into meter and centimeter.
feet=int(input("enter the feet: "))
inches=int(input("enter the inches: "))

total_meters = (feet * 0.3048) + (inches * 0.0254)
meter=int(total_meters)
centimeter=(total_meters-meter)*100
print("meter",meter,"centimeter",centimeter)
