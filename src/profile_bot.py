import io
import cProfile
from pstats import Stats, SortKey
from pathlib import Path

from rlbot.agents.base_agent import SimpleControllerState

from bot import Otter

current_dir = Path(__file__).parent.absolute()
DATA_FILE = current_dir / "profile_data.dat"
TEXT_FILE = current_dir / "profile_data.txt"
MATCH_CONFIG = current_dir / "profile_match.cfg"

MAX_FRAMES = 30_000


class OtterProfiler(Otter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__frame = 0
        self.__pr = cProfile.Profile()
        self.__saved_stats = False
        print("Starting profiling")

    def get_output(self, game_tick_packet) -> SimpleControllerState:
        output = None
        if self.__frame < MAX_FRAMES:
            self.__pr.enable()
            output = super().get_output(game_tick_packet)
            self.__pr.disable()

        elif not self.__saved_stats:
            print("Profiling done, saving data!")
            io_string = io.StringIO()
            ps = Stats(self.__pr, stream=io_string)
            ps.sort_stats(SortKey.TIME)
            ps.dump_stats(DATA_FILE)
            ps.print_stats()
            with open(TEXT_FILE, "w") as f:
                f.write(io_string.getvalue())
            self.__saved_stats = True
            print("Done! You can end the match now.")

        self.__frame += 1
        return output if output is not None else super().get_output(game_tick_packet)


if __name__ == "__main__":

    from rlbot.setup_manager import SetupManager

    manager = SetupManager()
    manager.load_config(config_location=MATCH_CONFIG)
    manager.connect_to_game()
    manager.launch_early_start_bot_processes()
    manager.start_match()
    manager.launch_bot_processes()
