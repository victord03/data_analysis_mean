from typing import Tuple, List
from math import sqrt
from pysnooper import snoop

def main():

    # data
    frequencies = 2, 1, 1, 2, 4, 3
    ranges = (5, 9), (10, 14), (15, 19), (20, 24), (25, 29), (30, 35)

    # operations
    sum_of_frequencies = calc_sum(frequencies)
    m = calc_average_values(ranges)
    f_times_m = calc_f_times_m(frequencies, m)
    sum_f_times_m = calc_sum(tuple(f_times_m))
    x_bar = round(sum_f_times_m / sum_of_frequencies, 1)

    highest_value, this_range, median_result = calc_mode(frequencies, ranges, also_median=False)

    # median_for_overall_interval = round((1/2 * sum_of_frequencies), 1)

    # todo: one-liner for sigma ?
    # var = round(sqrt(calc_sum(tuple([(x-x_bar)**2 for x in m])) / sum_of_frequencies - 1), 1)

    sigma = calc_sigma(m, x_bar, sum_of_frequencies)


    # display
    print_highest_value = False
    if print_highest_value:
        print(
            "\n\r\t\tHighest value \'"
            + str(highest_value)
            + "\' found at range \'"
            + str(this_range)
            + "\'\n"
        )

    printing = True
    if printing:
        print(
            f"\n\t{frequencies=}, {ranges=}"
            + f"\n\t\tSUM(f) = "
            + str(sum_of_frequencies)
            + f"\n\n\t\tMedian value per interval (m) : "
            + str(m)
            + f"\n\n\t\tx(bar) = SUM(f * m) / SUM(f) = "
            + str(x_bar)
            + f"\n\n\t\tsigma = "
            + str(sigma)
        )

# @snoop()
def calc_sum(numbers: Tuple) -> float:

    result = 0

    for value in numbers:
        result += value

    return result

def calc_cumulative_frequency(frequencies: List) -> list:

    i = 0

    cumulative_values_list = []

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

def calc_mode(frequencies: Tuple, ranges: Tuple, also_median=False):

    highest_value = 0
    index = None

    for i, value in enumerate(frequencies):

        if int(value) > highest_value:
            index = i
            highest_value = int(value)
        elif int(value == highest_value):
            # todo: accounted for duplicates
            pass

    median_value_encountered_at_index = None

    if also_median:

        cf = calc_cumulative_frequency(list(frequencies))

        for index, value in enumerate(cf):

            if value > int(calc_sum(frequencies) / 2):
                median_value_encountered_at_index = ranges[index-1]
            elif value == int(calc_sum(frequencies)):
                median_value_encountered_at_index = ranges[index]


    return int(highest_value), ranges[index], median_value_encountered_at_index

def calc_f_times_m(f: Tuple, m: List) -> List:

    f_times_m = list()

    for index, item in enumerate(m):
        f_times_m.append(item * f[index])

    return f_times_m

def calc_sigma(m: List, x_bar: float, sum_frequencies: float) -> float:

    step_1 = [(x-x_bar)**2 for x in m]
    step_2 = [x*sum_frequencies for x in step_1]

    numerator = round(calc_sum(tuple(step_2)) / len(step_2), 1)

    return round((sqrt(numerator / sum_frequencies - 1)), 1)

if __name__ == "__main__":
    main()
