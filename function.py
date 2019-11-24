# print the square for each value
#function
def square(x):
    return x*x
#loop the value from input
# providing an main function in python
def main():
    range_val = input("Enter the range value: ")
    range_val = int(range_val)
    for i in range(range_val):
        print("{} square is {}".format(i, square(i)))
if __name__ == "__main__":
    main()
