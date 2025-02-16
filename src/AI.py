from src.client import GameClient
from src.model import GameView
from src.memory import memory as Memory
from src import game as Game
from src import tools

log = tools.Logger()
mem = Memory.Memory()





def get_thief_starting_node(view: GameView) -> int:
    # write your code here
    log.setup(view.viewer)
    game = Game(view)
    mem.update(game)

    return 2


class Phone:
    def __init__(self, client: GameClient):
        self.client = client

    def send_message(self, message):
        self.client.send_message(message)


class AI:
    def __init__(self, phone: Phone):
        self.phone = phone

    def thief_move_ai(self, view: GameView) -> int:
        # write your code here
        log.setup(view.viewer)
        game = Game(view)
        mem.update(game)

        message = ''
        for m in range(len(view.visible_agents)):
            message = message  + '0'
        self.phone.send_message(message)
        return 2

    def police_move_ai(self, view: GameView) -> int:
        # write your code here
        log.setup(view.viewer)
        game = Game(view)
        mem.update(game)

        self.phone.send_message('00101001')
        return 1
