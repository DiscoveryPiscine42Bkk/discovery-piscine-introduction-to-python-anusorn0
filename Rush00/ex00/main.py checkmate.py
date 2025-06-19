def is_king_in_check(board):
    # Find the position of the King ('K')
    king_position = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        print("Error: No King found on the board!")
        return

    # Get the row and column of the King
    king_row, king_col = king_position

    # Directions for Rook, Queen (vertical and horizontal)
    directions = [
        (-1, 0), (1, 0),  # vertical (up and down)
        (0, -1), (0, 1)   # horizontal (left and right)
    ]
    
    # Diagonal directions for Bishop, Queen
    diagonal_directions = [
        (-1, -1), (-1, 1),  # top-left, top-right
        (1, -1), (1, 1)     # bottom-left, bottom-right
    ]
    
    # Check for Rooks and Queens horizontally and vertically
    for dr, dc in directions:
        r, c = king_row + dr, king_col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            piece = board[r][c]
            if piece != '.':
                if (piece == 'R' or piece == 'Q'):  # Rook or Queen can attack vertically or horizontally
                    print("Success")
                    return
                break  # Stop checking further if an obstructing piece is encountered
            r += dr
            c += dc

    # Check for Bishops and Queens diagonally
    for dr, dc in diagonal_directions:
        r, c = king_row + dr, king_col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            piece = board[r][c]
            if piece != '.':
                if (piece == 'B' or piece == 'Q'):  # Bishop or Queen can attack diagonally
                    print("Success")
                    return
                break  # Stop checking further if an obstructing piece is encountered
            r += dr
            c += dc

    # Check for Pawns attacking diagonally (only one step away)
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = king_row + dr, king_col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            piece = board[r][c]
            if piece == 'P':  # Pawn can only attack diagonally
                print("Success")
                return

    # If no piece can attack the King
    print("Fail")