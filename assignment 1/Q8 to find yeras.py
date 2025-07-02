days=int(input("Enter no of days"))

years=days//365
days=days%365
week=days//7
days=days%7
print("years",years,"week",week,"days",days)