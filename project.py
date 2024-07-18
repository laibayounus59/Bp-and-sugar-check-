#For BP
systolic = int(input("Enter systolic pressure: "))
diastolic = int(input("Enter diastolic pressure: "))
if systolic < 120 and diastolic < 80:
  bp_result = "Normal"
elif systolic < 130 and diastolic < 80:
  bp_result = "Higher"
elif systolic < 140 or diastolic < 90:
  bp_result = "Stage 1 Hypertension"
else:
  bp_result = "Stage 2 Hypertension"
#For blood sugar
bs_level = int(input("Enter blood sugar level: "))
if bs_level < 140:
  bs_result = "Normal"
elif bs_level < 180:
  bs_result = "Prediabetic"
else:
  bs_result = "Diabetic"
print(f"Your blood pressure is: {bp_result}")
print(f"Your blood sugar level is: {bs_result}")
