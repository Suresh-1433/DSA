def get_series_sum(number,sum):
    if number < 1:
        return sum 
    sum = sum + (1/number)
    return get_series_sum(number-1,sum)

number = int(input())
sum = 0
series_sum = get_series_sum(number,sum)

print(f"{series_sum:.2f}")

