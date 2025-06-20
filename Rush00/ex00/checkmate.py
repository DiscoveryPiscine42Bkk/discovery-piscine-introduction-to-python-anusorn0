def checkmate(board: str):
    board = board.strip().split('\n')
    size = len(board)

    for row in board:
        if len(row) != size:
            print("Error")
            return

    king_pos = None  # หาตำแหน่งของ k ว่าอยู่ไหน
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < len(board[x])
    
    def is_pawn_attacking(): # ตรวจ Pawn (P) โจมตี
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True
        return False

    def is_bishop_attacking(): # ตรวจหา bishop (B) Queen (Q) โจมตี ทแยง
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'B' or piece == 'Q':
                    return True
                else:
                    break
        return False

    def is_rook_attacking(): # ตรวจหา rook และ Queen (Q) โจมตี แนวตรง
        x, y = king_pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'R' or piece == 'Q':
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")