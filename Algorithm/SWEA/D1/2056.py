d_31 = ['01', '03', '05', '07', '08', '10', '12']
d_30 = ['04', '06', '09', '11']

def calender(input_str):
    input_y = input_str[:4]
    input_m = input_str[4:6]
    input_d = input_str[6:]

    if input_m not in d_31 and input_m not in d_30 and input_m != '02':
        return -1
    elif input_m in d_31:
        if int(input_d) < 1 or int(input_d) > 31:
            return -1
    elif input_m in d_30:
        if int(input_d) < 1 or int(input_d) > 30:
            return -1 
    elif input_m == '02':
        if int(input_d) < 1 or int(input_d) > 28:
            return -1
    return input_y, input_m, input_d

T = int(input())

case_lst = []

for i in range(T):
    case_lst.append(input())

for i in range(len(case_lst)):
    if calender(case_lst[i]) == -1:
        print(f'#{i+1} -1')
    else:
        ans_year, ans_mon, ans_day = calender(case_lst[i])
        print(f'#{i+1} {ans_year}/{ans_mon}/{ans_day}')