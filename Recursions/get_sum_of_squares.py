def get_sum_of_squares(numbers,length,sum):
    if length < 0:
        return sum
    
    x =numbers[length]
    sum = sum + x*x
   
    return get_sum_of_squares(numbers,length-1,sum)

numbers = list(map(int,input().split()))

squares_sum =get_sum_of_squares(numbers,len(numbers)-1,0)
print(squares_sum)