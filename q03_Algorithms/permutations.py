import sys



def process_line(line):
    """Generate permutations and sort in alphabetical order"""
    print("processing line...")
    return



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python permutations.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                result = process_line(line)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)

