def find_median_sorted_arrays(
        num1: list[int],
        num2: list[int]) -> float:

    if not num1:
        if len(num2) % 2 == 0:
            return (num2[len(num2) //2] + num2[len(num2) //2 - 1]) / 2
        else:
            return num2[len(num2) //2]
    if not num2:
        if len(num1) % 2 == 0:
            return (num1[len(num1) //2] + num1[len(num1) //2 - 1]) / 2
        else:
            return num1[len(num1) //2]

    #swap the 2 arrays to make sure num1 is always the shortest
    if len(num2) <= len(num1):
        num_short, num_long = num2, num1
    else:
        num_short, num_long = num1, num2

    #how many numbers should be placed on the left sides
    total_numbers_on_left = (len(num_short) + len(num_long) + 1) // 2

    #lower and higher boundary of the shorter array
    low_boundary = 0
    high_boundary = len(num_short)

    while low_boundary <= high_boundary:
        partition_short = (low_boundary + high_boundary) // 2
        partition_long = total_numbers_on_left - partition_short

        if partition_short == 0:
            short_left_max = float('-inf')
        else:
            short_left_max = num_short[partition_short - 1]

        if partition_long == 0:
            long_left_max = float('-inf')
        else:
            long_left_max = num_long[partition_long - 1]

        if partition_short >= len(num_short):
            short_right_min = float('inf')
        else:
            short_right_min = num_short[partition_short]

        if partition_long >= len(num_long):
            long_right_min = float('inf')
        else:
            long_right_min = num_long[partition_long]

        if short_left_max <= long_right_min and long_left_max <= short_right_min:
            if (len(num_short) + len(num_long)) % 2 == 0:
                return (max(short_left_max, long_left_max) + min(short_right_min, long_right_min)) / 2
            else:
                return max(short_left_max, long_left_max)

        if short_right_min < long_left_max:
            low_boundary = partition_short + 1
        if long_right_min < short_left_max:
            high_boundary = partition_short - 1

    partition_long = total_numbers_on_left - len(num_short)
    if (len(num_short) + len(num_long)) % 2 == 0:
        return (num_long[partition_long - 1] + num_long[partition_long]) / 2
    else:
        return num_long[partition_long - 1]

if __name__ == '__main__':
    #num1 = [1,2,3,4,5]
    #num2 = [6,7,8,9,10,11,12,13,14,15,16,17]
    num1 = [5,6]
    num2 = [1,2,3,4,7]
    print(find_median_sorted_arrays(num1, num2))