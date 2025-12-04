import random


def make_board(rows, columns):
    """
    Create a board where each row and column pair is a coordinate that contains a randomized room description.

    :param rows: a positive integer that represents the number of rows on the board.
    :param columns: a positive integer that represents the number of columns on the board.
    :precondition: rows and columns are integers.
    :postcondition: generate a complete game board with the size of the given rows and columns
                    where each coordinate contains a room description
    :return: a dictionary representing the complete game board
    """
    rooms = ["Grand Hall of Still Time — silent clocks hang frozen mid-tick.",
             "Hidden Study — old books hum with shifting letters.",
             "Hall of Mirrors — your reflection moves before you do.",
             "Tarot Club Chamber — empty chairs face a burning candle.",
             "Detective’s Office — dust and tobacco scent linger faintly.",
             "Mirror Room — faces appear, vanish, and smile unseen.",
             "Whispering Parlor — voices murmur half-remembered tales.",
             "Wax Workshop — figures melt under trembling lamplight.",
             "Frozen Clock Tower — gears hover, time holds its breath.",
             "Masked Tavern — unseen guests laugh over invisible drinks.",
             "Moonlit Garden — pale flowers sway in still air.",
             "Living Newsroom — papers rewrite the present endlessly.",
             "Antique Shop — relics whisper names you don’t know.",
             "Empty Room — only your breath disturbs the quiet.",
             "Foggy Alley — gaslight flickers over wet cobblestone.",
             "Abandoned Cathedral — shattered glass glows like moonlight.",
             "Aurora Tunnel — runes pulse faintly in the dark.",
             "Alchemy Lab — potions swirl with mirrored colors.",
             "Forbidden Library — books hum prayers under your gaze.",
             "Opera Hall — curtains ripple without wind or sound.",
             "Steam Control Room — pipes sigh like restless spirits.",
             "Séance Chamber — candles flicker against the unseen.",
             "Runed Gate — symbols flash as you look away.",
             "Obsidian Bridge — steps shimmer like liquid silver.",
             "Hall of the Monocled Gentleman — someone watches from the glass."]
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = random.choice(rooms)
    return board