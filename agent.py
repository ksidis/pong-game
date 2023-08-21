from constants import Player, PADDLE_HEIGHT


class BaseAgent:
    def __init__(self) -> None:
        self.agent_type = None

    def tick(self, state) -> None:
        pass


class HumanAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self.agent_type = Player.HUMAN


class CpuAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__()
        self.agent_type = Player.AI

    def tick(self, state) -> None:
        if state.ball.position.y > state.r_paddle.y + ((PADDLE_HEIGHT * 2)// 3):
            state.r_paddle.move(up=False)
        elif state.ball.position.y < state.r_paddle.y + (PADDLE_HEIGHT// 3):
            state.r_paddle.move(up=True)
        else:
            pass

