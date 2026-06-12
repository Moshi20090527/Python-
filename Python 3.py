pay = int(input("請輸入消費金額"))
input ("按下空格鍵執行下一步")
pro = (input("您是否為會員（輸入Y or N）"))
#以下是if
if pro == "Y" and pay > 1000: 
   print ("最終金額:",int(pay*0.8))
elif pro == "Y" and pay < 1000:
     print ("最終金額:",int(pay*0.9))
else:  
     print ("最終金額:",pay) 
