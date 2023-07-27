from celery import shared_task


@shared_task
def divide(x, y):
    """
    Divide two numbers and return the result.

    Parameters:
    x (int or float): The numerator.
    y (int or float): The denominator.

    Returns:
    float: The result of dividing x by y.
    """
    import time

    time.sleep(5)
    return x / y
