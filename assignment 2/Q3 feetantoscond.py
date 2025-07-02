feet=int(input("Enter the feet :"))
inches=int(input("Enter the inches :"))

total_meters=(feet * 0.3048) + (inches * 0.0254)
meter=int(total_meters)
centimeter=(total_meters)*100
print("meter",meter,"centimeter",centimeter)