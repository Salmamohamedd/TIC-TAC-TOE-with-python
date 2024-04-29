from project import check_winner, check_state, bestMove

def test_check_winner():
    assert check_winner(['X', 'O', 'X', 'O', 'X', 6, 7, 'O', 'X']) == 'X wins'
    assert check_winner(['X', 'X', 'O', 'X', 'O', 'X', 'O', 8, 'O']) == 'O wins'
    assert check_winner(['X', 'O', 'O', 'X', 'X', 'O', 'X', 8, 9]) == 'X wins'


def test_check_state():
    assert check_state(['X', 'O', 'X', 'O', 'X', 6, 7, 'O', 'X']) == 2
    assert check_state(['X', 'X', 'O', 'X', 'O', 'X', 'O', 8, 'O']) == -2
    assert check_state(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']) == 0



def test_bestMove():
    assert bestMove([1, 2, 3, 4, 'x', 6, 7, 8, 9]) == 8
    assert bestMove(['X', 2, 3, 4, 5, 6, 7, 8, 9]) == 4