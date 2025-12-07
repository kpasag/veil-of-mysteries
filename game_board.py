"""
Kyle Pasag
A01428389

Module for creating the game board.

This module generates the dictionary-based grid that represents all playable
positions in the world map. Each coordinate pair is assigned a randomly
selected room description that the player can explore during the game.
"""
import random
import messages


def make_board(rows: int, columns: int) -> dict[tuple[int, int], str]:
    """
    Create a board where each row and column pair is a coordinate that contains a randomized room description.

    :param rows: a positive integer that represents the number of rows on the board.
    :param columns: a positive integer that represents the number of columns on the board.
    :precondition: rows and columns are integers.
    :postcondition: generate a complete game board with the size of the given rows and columns
                    where each coordinate contains a room description
    :return: a dictionary representing the complete game board
    """
    rooms = messages.get_list_of_message_from_json("rooms")
    board = {(row, column): random.choice(rooms)
             for row in range(rows)
             for column in range(columns)}
    return board