def multi_table():
    """Plan is to create a 9x9 multiplication table"""    
    rows, cols = 9, 9
    r = 1 
    while r <= 9:
        c = 1
        print("[", r, "]", end= "  ")
        while c <= 9:
            # print("cols:", c)
            output = r * c
            print(output, end="  ")
            c += 1
        print()
        r += 1
    
        # 1x1=9
multi_table()

# rows, cols = 5, 5
# r = 0
# while r < rows:
#     c = 0
#     while c < cols:
#         output = (r * c) + "   "
#         print(output, end="")
#         c += 1
#     print("\n")
#     r += 1
