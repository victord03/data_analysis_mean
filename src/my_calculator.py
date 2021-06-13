from typing import Tuple, List
from math import sqrt
from pysnooper import snoop

def main():

    # data
    frequencies = 3, 5, 9, 12, 8
    ranges = (50, 59), (60, 69), (70, 79), (80, 89), (90, 100)

    # operations
    sum_of_frequencies = calc_sum(frequencies)
    m = calc_average_values(ranges)
    f_times_m = calc_f_times_m(frequencies, m)
    sum_f_times_m = calc_sum(tuple(f_times_m))
    mean = round(sum_f_times_m / sum_of_frequencies, 1)

    standard_deviation = calc_standard_deviation(frequencies, m, mean, sum_of_frequencies)

    # cumulative_freq = calc_cumulative_frequency(list(frequencies))
    # highest_occurrence = find_highest_value(frequencies)


    # display
    printing = True
    if printing:
        print(
            "\n\tNumber of class ranges: "
            + str(len(frequencies))
            + "\n\tSum of frequencies: "
            + str(sum_of_frequencies)
            + "\n\tm: "
            + str(m)
            + "\n\tf times m: "
            + str(f_times_m)
            + "\n\tsum_of_frequencies of (f times m): "
            + str(sum_f_times_m)
            + "\n\tmean: "
            + str(mean)
            + "\n\tstandard deviation: "
            + str(standard_deviation)
        )


# @snoop()
def calc_sum(numbers: Tuple) -> float:

    result = 0

    for value in numbers:
        result += value

    return result

def calc_cumulative_frequency(frequencies: List) -> list:

    i = 0

    cumulative_values_list = list()

    for frequency in frequencies:
        if i == 0:
            cumulative_values_list.append(frequency)
        else:
            cumulative_values_list.append(cumulative_values_list[i-1] + frequency)

        i += 1

    return cumulative_values_list

# @snoop()
def calc_average_values(ranges: Tuple) -> List:

    results_list = list()

    for current_tuple in ranges:
        results_list.append((current_tuple[0] + current_tuple[1]) / 2)

    return results_list

def find_highest_value(values: Tuple) -> int:

    highest_value = 0

    for value in values:

        if int(value) > highest_value:
            highest_value = int(value)

    return int(highest_value)

def calc_f_times_m(f: Tuple, m: List):

    f_times_m = list()

    for index, item in enumerate(m):
        f_times_m.append(item * f[index])

    return f_times_m

def calc_m_minus_mean(m: List, mean: float) -> List:

    result = list()

    for value in m:
        result.append(round(value - mean, 1))

    return result

def calc_f_times_m_minus_mean(f: Tuple, m_minus_mean: List) -> List:

    result = list()

    for index, value in enumerate(f):
        result.append(round(value * m_minus_mean[index], 1))

    return result

def calc_standard_deviation(f: Tuple, m: List, x_bar: float, n: float) -> float:

    list_of_m_minus_mean = calc_m_minus_mean(m, x_bar)
    list_of_m_minus_mean_squared = [round(x**2, 1) for x in list_of_m_minus_mean]

    list_of_f_times_m_minus_mean_squared = calc_f_times_m_minus_mean(f, list_of_m_minus_mean_squared)

    sum_of_list_of_f_times_m_minus_mean_squared = calc_sum(tuple(list_of_f_times_m_minus_mean_squared))

    return round(sqrt(sum_of_list_of_f_times_m_minus_mean_squared / n - 1), 1)

if __name__ == "__main__":
    main()
