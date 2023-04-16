def read_input():
    inp = input()
    if "F" in inp:
        path = "./tests/" + "06"
        with open(path, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return (pattern, text)
    if "I" in inp:
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)
    return (input().rstrip(), input().rstrip())

def print_results(output):
    print(' '.join(map(str, output)))

def rabin_karp(pattern: str, text: str) -> list:
    B = 13
    Q = 256

    patt = len(pattern)
    txt = len(text)

    multiplier = 1
    for i in range(1, patt):
        multiplier = (multiplier * B) % Q

    pattern_hash = hash_str(pattern)
    text_hash = hash_str(text[:patt])

    results = []
    for i in range(txt - patt + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+patt]:
                results.append(i)
        if i < txt - patt:
            text_hash = ((text_hash - ord(text[i]) * multiplier) * B + ord(text[i+patt])) % Q

    return results

def hash_str(string: str) -> int:
    B = 13
    Q = 256
    result = 0
    for i in range(len(string)):
        result = (B * result + ord(string[i])) % Q
    return result

if __name__ == '__main__':
    print_results(rabin_karp(*read_input()))