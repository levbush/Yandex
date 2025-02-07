data = input().split()
halflife = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
layer_map = input().split()
radioactive_layer_map = list(map(float, input().split()))
max_sum = float(input())
min_days = 0
days_to_halflife = halflife.copy()
while round(sum(radioactive_layer_map), 10) > max_sum:
    halflife_today = min(days_to_halflife.values())
    elements_today = [k for k, v in days_to_halflife.items() if v == halflife_today]
    min_days += halflife_today
    for i in range(len(layer_map)):
        if layer_map[i] in elements_today:
            radioactive_layer_map[i] /= 2
    days_to_halflife = {
        k: v - halflife_today if halflife_today < v
        else halflife[k] + (v - halflife_today)
        for k, v in days_to_halflife.items()
    }
print(min_days)
print(*radioactive_layer_map)