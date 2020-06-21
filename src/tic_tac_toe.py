import logging
import random
import sys


class TicTacToe:
    player_char = 'x'
    ai_char = 'o'

    board = {
        1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    }

    winning_patterns = [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9},
        {1, 5, 9},
        {3, 7, 5},
    ]

    def __init__(self):
        self.logger = self.create_logger()

    @staticmethod
    def create_logger() -> logging:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        return logging.getLogger(__name__)

    def run(self) -> None:
        while True:
            self.logger.debug(f"STATE: {self.board}")
            self.logger.info(self.draw_board())

            self.move()
            if self.check_if_player_wins(self.player_char):
                self.logger.info(self.draw_board())
                self.logger.info('You won.')
                return

            if not self.available_positions():
                self.logger.info('Draw.')
                return

            self.ai_move()
            if self.check_if_player_wins(self.ai_char):
                self.logger.info(self.draw_board())
                self.logger.info('You lost. Kind of impossible but...')
                return

    def draw_board(self) -> str:
        board = "\n"
        for position in self.board:
            board += f"|{self.board[position]}"
            if (position % 3) == 0:
                board += '|\n'
        return board

    def move(self) -> None:
        try:
            position = int(input("Enter position: "))
            if not self.board[position].isnumeric():
                self.logger.error('Already played.')
                raise ValueError

            if position in range(1, 10):
                self.board[position] = self.player_char
        except (KeyError, ValueError):
            self.logger.info("1 to 9 only, try again")
            self.move()

    def player_pattern(self, char) -> set:
        return {item[0] for item in self.board.items() if item[1] == char}

    def check_if_player_wins(self, char) -> bool:
        player_pattern = self.player_pattern(char)
        for pattern in self.winning_patterns:
            if len(pattern - player_pattern) == 0:
                return True

    def ai_move(self) -> None:
        bot_move = random.choice(list(self.available_positions()))
        self.board[bot_move] = self.ai_char

    def available_positions(self) -> set:
        return {item[0] for item in self.board.items() if item[1].isnumeric()}


def main():
    game = TicTacToe()
    game.run()


if __name__ == '__main__':
    main()
