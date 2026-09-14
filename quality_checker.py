print("Smart Manufacturing Quality Checker")
print("-----------------------------------")
part_name = input("Enter the part name: ")
length = float(input("Enter the part length in cm: "))
width = float(input("Enter the part width in cm: "))
weight = float(input("Enter the part weight in grams: "))
min_length = 10.0
max_length = 10.5
min_width = 5.0
max_width = 5.5
min_weight = 20.0
max_weight = 25.0
if min_length <= length <= max_length:
  length_result = "PASS"
else:
  length_result = "FAIL"
if min_width <= width <= max_width:
  width_result = "PASS"
else:
  width_result = "FAIL"
if min_weight <= weight <= max_weight:
  weight_result = "PASS"
else:
  weight_result = "FAIL"
if length_result == "PASS" and width_result == "PASS" and weight_result == "PASS":
  overall_result = "PASS"
else:
  overall_result = "NEEDS INSPECTION"
print()
print("QUALITY CHECK RESULTS")
print("---------------------")
print("Part:", part_name)
print("Length:", length_result)
print("Width:", width_result)
print("Weight:", weight_result)
print("Overall Result:", overall_result)
if overall_result == "PASS":
  print("This part meets all quality standards.")
else:
  print("This part should be inspected before use.")
