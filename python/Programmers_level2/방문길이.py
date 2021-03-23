def solution(dirs):
    cur_x = 0
    cur_y = 0
    visited = []

    for i in dirs:
        next_x = cur_x
        next_y = cur_y

        if i == 'L':
            next_x -= 1
        elif i == 'R':
            next_x += 1
        elif i == 'U':
            next_y += 1
        else:
            next_y -= 1

        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue
        else:   # UDU 같이 갔던 길 돌아오는 경우도 고려
            if (cur_x, cur_y, next_x, next_y) not in visited and (next_x, next_y, cur_x, cur_y) not in visited:
                visited.append((cur_x, cur_y, next_x, next_y))
            cur_x, cur_y = next_x, next_y

    return len(visited)

# 추천 풀이
'''
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
'''