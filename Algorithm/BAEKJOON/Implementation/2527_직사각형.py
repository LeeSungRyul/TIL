T = 4

for tc in range(T):
    sq1_xmin, sq1_ymin, sq1_xmax, sq1_ymax, sq2_xmin, sq2_ymin, sq2_xmax, sq2_ymax = map(
        int, input().split()
    )

    if sq1_xmax < sq2_xmin or sq2_xmax < sq1_xmin or sq1_ymax < sq2_ymin or sq2_ymax < sq1_ymin:
        ans = "d"
    elif (
        (sq1_xmax == sq2_xmin and sq1_ymax == sq2_ymin)
        or (sq1_xmin == sq2_xmax and sq1_ymax == sq2_ymin)
        or (sq2_xmax == sq1_xmin and sq2_ymax == sq1_ymin)
        or (sq2_xmin == sq1_xmax and sq2_ymax == sq1_ymin)
    ):
        ans = "c"
    elif (
        (sq1_ymin == sq2_ymax and (sq1_xmin < sq2_xmin or sq2_xmin < sq1_xmax))
        or (sq1_ymin == sq2_ymax and (sq1_xmin < sq2_xmax or sq2_xmax < sq1_xmax))
        or (sq1_xmax == sq2_xmin and (sq1_ymin < sq2_ymin or sq2_ymin < sq1_ymax))
        or (sq1_xmax == sq2_xmin and (sq1_ymin < sq2_ymax or sq2_ymax < sq1_ymax))
        or (sq2_ymin == sq1_ymax and (sq2_xmin < sq1_xmin or sq1_xmin < sq2_xmax))
        or (sq2_ymin == sq1_ymax and (sq2_xmin < sq1_xmax or sq1_xmax < sq2_xmax))
        or (sq2_xmax == sq1_xmin and (sq2_ymin < sq1_ymin or sq1_ymin < sq2_ymax))
        or (sq2_xmax == sq1_xmin and (sq2_ymin < sq1_ymax or sq1_ymax < sq2_ymax))
    ):
        ans = "b"
    else:
        ans = "a"

    print(ans)
