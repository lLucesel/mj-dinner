import _ran

list_a = [512, 356, 477, 611, 532, 453, 499, 378, 561, 444, 531, 601, 387, 426, 468]
list_b = [95, 142, 111, 132, 128, 89, 121, 99, 104, 71, 101, 130, 95, 108, 102]

result_a = []
result_b = []
total_sum = 0

while len(result_a) < 7 or len(result_b) < 7:
    selected_list = random.choice([list_a, list_b])
    selected_number = random.choice(selected_list)

    if selected_list is list_a and len(result_a) < 7 and sum(result_a) + selected_number >= 4000:
        result_a.append(selected_number)
        total_sum += selected_number
    elif selected_list is list_b and len(result_b) < 7 and sum(result_b) + selected_number >= 4000:
        result_b.append(selected_number)
        total_sum += selected_number

print("랜덤하게 선택된 a의 숫자:", result_a)
print("랜덤하게 선택된 b의 숫자:", result_b)
print("a의 총합:", sum(result_a))
print("b의 총합:", sum(result_b))
print("총합:", total_sum)
