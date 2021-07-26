# ord(A) = 65 --> A = 1
def change_str(input_str):
    ans_lst = []
    for s in input_str:
        ans_lst.append(str(ord(s) - 64))
    return ans_lst

input_str = input()

print(' '.join(change_str(input_str)))