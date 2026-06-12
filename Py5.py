print ("請輸入你的年齡")
age_str = input ()
age = int(age_str)
if age < 12:
   print ("半票") 
elif age >= 12 and age < 65:
     print ("全票") 
elif age >65:
     print ("老人票") 
