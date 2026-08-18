def divide_numbers(a: str, b: str) -> None:
    try:
        a_int = int(a) # convert strings to integers
        b_int = int(b)
        result = a_int / b_int # store the integer division in result
        print(result)

        # error handling
    except Exception as error:
        print("An error occurred:", error)

# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
