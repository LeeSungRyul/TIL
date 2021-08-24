def change_experession(original):
    stack = []
    priority = {
        "+": 0,
        "*": 1,
    }  # +, -, *, / 만 딕셔너리로 가능하고, 괄호는 여는 괄호는 무조건 append, 닫는 괄호는 ) 나올 때까지 pop해야 하므로 별도 취급
    result = ""

    for i in range(N):
        if original[i].isdigit():
            result += original[i]
        else:
            if original[i] == "(":
                stack.append(original[i])
            elif original[i] == ")":
                while True:
                    temp = stack.pop()
                    if temp == "(":
                        break
                    result += temp
            else:
                if not stack:
                    stack.append(original[i])
                else:
                    if stack[-1] == "(" or priority[original[i]] > priority[stack[-1]]:
                        stack.append(original[i])
                    else:
                        while True:
                            result += stack.pop()
                            if (
                                not stack
                                or stack[-1] == "("
                                or priority[original[i]] > priority[stack[-1]]
                            ):
                                stack.append(original[i])
                                break
    if stack:
        while stack:
            result += stack.pop()

    return result


def calc_expression(expression):
    stack = []

    for i in range(len(expression)):
        if expression[i].isdigit():
            stack.append(expression[i])
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if expression[i] == "+":
                stack.append(num1 + num2)
            elif expression[i] == "*":
                stack.append(num1 * num2)

    return stack


T = 10

for tc in range(1, T + 1):
    N = int(input())
    original = input()
    changed = change_experession(original)
    ans = calc_expression(changed)

    print("#{} {}".format(tc, *ans))
