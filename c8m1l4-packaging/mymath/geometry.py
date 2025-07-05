def area_of_rectangle(l, w):
    """
    This function returns the mean of the given list of numbers.
    The mean is calculated as the sum of all numbers divided by the count of numbers.
    """
    # Calculate the mean by summing all the numbers and dividing by the length of the list.
    # 'sum(numbers)' computes the total of all numbers in the list.
    # 'len(numbers)' gives the count of numbers in the list.
    # The mean (or average) is the total sum divided by the number of elements.
    return l * w  # Return the mean value.

def area_of_circle(radius):
    """
    This function returns the median of the given list of numbers.
    The median is the middle value when the numbers are sorted.
    If there is an even number of observations, it returns the average of the two middle numbers.
    """
    # Sort the list of numbers in ascending order.
    # Sorting is necessary to find the median, as the median depends on the order of values.
    PI = 3.14159

    # Return the calculated median value.
    return (radius ** 2) * PI
