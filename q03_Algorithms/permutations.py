import sys


def generatePerms(inputLine: str) -> set:
    """
    Generate all unique permutations of a string
    Returns a set of the permutations
    """
    if len(inputLine) <= 1:
        return {inputLine}
    
    result = set()
    for i, char in enumerate(inputLine):
        remaining = inputLine[:i] + inputLine[i+1:]
        for perm in generatePerms(remaining):
            result.add(char + perm)
    
    return result


def processLine(line: str) -> str:
    """
    Generates all unique permutations of the input string and sorts them in alphabetical order
    Returns a string of all permutations separated by comma
    """
    line = line.strip()
    if not line:
        return ""
    
    perms = generatePerms(line)     # Generate all unique permutations
    sortedPerms = sorted(perms)     # Python's default sort satistfies digits < uppercase < lowercase
    return ','.join(sortedPerms)


if __name__ == "__main__":
    # Read in file
    if len(sys.argv) != 2:
        print("Usage: python permutations.py <input_file.txt>")
        sys.exit(1)

    inputFile = sys.argv[1]

    # Go through each line in the file
    try:
        with open(inputFile, 'r') as file:
            for line in file:
                result = processLine(line)
                if result:          # Skips empty lines
                    print(result)
    except FileNotFoundError:
        print(f"Error: File '{inputFile}' not found")
        sys.exit(1)

