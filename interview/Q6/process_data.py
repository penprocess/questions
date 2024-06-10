import sys

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        reversed_string = reverse_string(input_file)
        print(reversed_string)