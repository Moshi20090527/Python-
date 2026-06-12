user_str = input("請問有買門票嗎？（Y OR N）")
#if 
if user_str == "Y":
   X_str = input ("是否攜帶違禁品(Y or N)")
   age = int(input("請輸入年齡"))
   if X_str == "Y":
        print ("攜帶違禁品，禁止入場")
   elif age < 12:
             print ("年齡太小，需家長陪同") 
   else:
      print ("歡迎入場，祝您觀賽愉快")   
else:
  print ("請至櫃檯購買門票")     
