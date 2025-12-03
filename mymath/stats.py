"""Module for statistical calculations like mean and median."""


def mean(numbers):
    """
    Calculate the mean of a list of numbers.

    The mean is the sum of all numbers divided by their count.
    """
    # Sum all numbers and divide by the count to get the mean.
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Calculate the median of a list of numbers.

    The median is the middle value after sorting the numbers.
    If there's an even count, it's the average of the two middle numbers.
    """
    # Sort the numbers to find the median.
    numbers.sort()

    # If the list has an even number of elements.
    if len(numbers) % 2 == 0:
        # Get the two middle elements.
        mid1_index = len(numbers) // 2
        mid2_index = mid1_index - 1
        median1 = numbers[mid1_index]
        median2 = numbers[mid2_index]

        # Calculate the average of the two middle numbers.
        mymedian = (median1 + median2) / 2
    else:
        # For an odd number of elements, return the middle one.
        mymedian = numbers[len(numbers) // 2]

    return mymedian
