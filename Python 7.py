from datetime import datetime
start_input= input("請輸入開始日期 年/月/日")
end_input= input("請輸入結束日期 年/月/日")

start_date= datetime.strptime(start_input,"%Y/%m/%d").date()
end_date= datetime.strptime(end_input,"%Y/%m/%d").date()

print(f"開始日期:{start_date}")
print(f"結束日期:{end_date}")

total_days=(end_date-start_date).days
print(f"還剩{day_left}天")
