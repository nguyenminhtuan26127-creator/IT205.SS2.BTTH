print("=== Nhập thông tin bệnh nhân ===")
name_pateint = input("Nhập vào tên bệnh nhân: ")
year_of_birth =  int(input("Nhập vào năm sinh bệnh nhân: "))
number_of_sick_days = int(input("Nhập vào số ngày bị bệnh: "))
body_temperature = float(input("Nhập vào nhiệt độ cơ thể(\u00B0C): "))
examination_costs = int(input("Nhập vào chi phí khám: "))

valid = True

if name_pateint == "":
    valid = False
    print("Tên bệnh nhân không được để trống!")

if year_of_birth < 1900 or year_of_birth > 2026:
    valid = False
    print("Năm sinh không hợp lệ!")

if number_of_sick_days < 0:
    valid = False
    print("Số ngày bệnh không phù hợp!")

if body_temperature < 30 or body_temperature > 45:
    valid = False
    print("Nhiệt độ cơ thể không hợp lý!")

if examination_costs <= 0:
    valid = False
    print("Chi phí khám không đúng!")

if  not valid:
    print("Thoát chương trình...")
    exit()
else:
    # Tuổi
    age = 2026 - year_of_birth

    # Trạng thái bệnh
    status = ""
    if body_temperature > 38 and number_of_sick_days > 3:
        status = "Nguy hiểm"
    elif body_temperature > 38:
        status = "Sốt cao"
    elif body_temperature > 37.5:
        status = "Sốt nhẹ"
    else:
        status = "Bình thường"

    # Mức đọ ưu tiên
    priority_level = ""
    if status == "Nguy hiểm":
        if age > 60:
            priority_level = "Cấp cứu"
        else:
            priority_level = "Ưu tiên cao"
    else:
        priority_level = "Bình thường"

    # Chi phí
    surcharge = examination_costs * 0.1
    total_cost = examination_costs + surcharge

    # Mức chi phí
    cost_level = ""
    if total_cost > 500000:
        cost_level = "Cao"
    else:
        cost_level = "Thấp"
    print("=== Kết quả ===")
    print(f"Tên: {name_pateint}")
    print(f"Tuổi: {age}")
    print(f"Nhiệt độ:{body_temperature}\u00B0C")
    print(f"\nTình trạng: {status}")
    print(f"Mức độ ưu tiên: {priority_level}")
    print(f"\n Tổng chi phí: {total_cost}")
    print(f"Mức chi phí: {cost_level}")
