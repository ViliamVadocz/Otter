import sys
import cProfile
from pathlib import Path

from rlbot.agents.standalone.standalone_bot import StandaloneBot, run_bot

from bot import Otter


class OtterProfileBot(StandaloneBot):
    def is_hot_reload_enabled(self):
        return False

    initialize_agent = Otter.initialize_agent
    get_output = Otter.get_output
    pick_strategy = Otter.pick_strategy
    render = Otter.render


def main():
    try:
        run_bot(OtterProfileBot)
    except Exception as err:
        print(err)


if __name__ == "__main__":

    config_path = (Path(__file__).parent / "bot.cfg").absolute()
    sys.argv[1:] = [
        f"--config-file={config_path}",
        "--player-index=0",
        "--team=0",
        "--spawn-id=1",
    ]
    cProfile.run("main()")
