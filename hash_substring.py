# python3

B = 13

def read_input():
    teksts = input()
    patt = ""
    string = ""

    if "I" in teksts:
        patt = input().strip()
        string = input().strip()
    elif "F" in teksts: 
        f = input().strip()
        with open("tests/" +f, 'r') as f:
            patt = f.readline().strip()
            string = f.readline().strip()
    
    return (patt, string)
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(patt, text):
    patt = len(patt)
    txt = len(text)

    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    return [0]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

