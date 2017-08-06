def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True

def next_prime(number):
	"""
	Print the closest prime number larger than *numbers*.
	You can call this function in the python shell with: print(next_prime(10))
	"""
	while True:
		number += 1
		if is_prime(number):
			return number
