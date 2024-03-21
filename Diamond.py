def print_diamond(n):
    if n % 2 == 0:
        n += 1  # Adjust for even-sized diamonds

    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(" " * spaces + "123" * stars)

# Test the function with various values of 'n'
print("Please enter the size of the diamond you want")
h = input(">")
n = int(h)

print_diamond(n)