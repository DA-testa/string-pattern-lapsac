# python3

B = 13
Q = 256

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

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(patt, text):
    patt = len(patt)
    txt = len(text)
    
    pattern_hash = 0
    for i in range(patt):
        pattern_hash = pattern_hash * B + ord(patt[i]) % Q

    text_hash = 0
    for i in range(patt):
        txt_hash = (txt_hash * B + ord(txt[i])) % Q   
    
    gadijumi = []

    for i in range(txt - patt +1):
        if pattern_hash == text_hash and patt == txt[i:i+patt]:
            gadijumi.append(i)
        if i < txt - patt:
            text_hash = ((text_hash - ord(text[i]) * pow(B, patt-1, Q)) * B + ord(text[i+patt])) % Q

    if gadijumi:
        return gadijumi
    else:
        return [0]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

