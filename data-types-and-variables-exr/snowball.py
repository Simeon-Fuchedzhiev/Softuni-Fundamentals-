num_snowball = int(input())
highest_value = 0

for i in range(num_snowball):
    snowball_weight_ = int(input())
    snowball_time_ = int(input())
    snowball_quality_ = int(input())
    
    snowball_value = int((snowball_weight_ / snowball_time_) ** snowball_quality_)
    if snowball_value > highest_value:
        highest_value = snowball_value
        snowball_weight = snowball_weight_
        snowball_time = snowball_time_
        snowball_quality = snowball_quality_
print(f"{snowball_weight} : {snowball_time} = {highest_value} ({snowball_quality})")
    