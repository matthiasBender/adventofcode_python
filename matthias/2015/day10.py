input = "1321131112"

def next_in_seq(s: str) -> str:
    result = ""
    last_c = s[0]
    count = 0
    for c in s:
        if last_c == c:
            count += 1
        else:
            result += str(count) + last_c
            count = 1
            last_c = c
    return result + str(count) + last_c
    
result = input
for _ in range(40):
    result = next_in_seq(result)

print("Rätsel 1: ", len(result))

result = input
for _ in range(50):
    result = next_in_seq(result)

print("Rätsel 2: ", len(result))
