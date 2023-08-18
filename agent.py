from constants import Player
from pong import Pong


class BaseAgent:
    def __init__(self) -> None:
        self.agent_type = None

    def tick(self, state:Pong) -> None:
        pass


class HumanAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self.agent_type = Player.HUMAN


class CpuAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self.agent_type = Player.AI

    def tick(self, state:Pong) -> None:
        if state.ball.position.y > state.r_paddle.y:
            state.r_paddle.move(up=False)
        else:
            state.r_paddle.move(up=True)

