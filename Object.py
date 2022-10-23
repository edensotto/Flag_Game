import consts


def is_touching_flag(row, col):
    if row >= consts.FLAG_START_ROW or row <= consts.FLAG_END_ROW:
        return True

    elif col >= consts.FLAG_START_COL or col <= consts.FLAG_END_COL:
        return True

    else:
        return False
