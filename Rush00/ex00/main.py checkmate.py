def checkmate(board_str):
    # แปลงข้อความเป็นตาราง 2 มิติ
    board = [list(row) for row in board_str.splitlines()]
    n = len(board)

    # หาตำแหน่งของ King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    # ถ้าไม่เจอ King เลย
    if not king_pos:
        print("Fail")
        return

    kr, kc = king_pos  # ตำแหน่งแถว/คอลัมน์ของ King

    # ฟังก์ชันตรวจว่าตำแหน่งอยู่ในกระดานไหม
    def inside(r, c):
        return 0 <= r < n and 0 <= c < n

    # ตรวจเบี้ย P (โจมตีเฉียงขึ้น)
    for dc in [-1, 1]:
        pr, pc = kr - 1, kc + dc
        if inside(pr, pc) and board[pr][pc] == 'P':
            print("Success")
            return

    # ยังไม่ตรวจ R, B, Q (คุณสามารถเพิ่มต่อได้)
    print("Fail")