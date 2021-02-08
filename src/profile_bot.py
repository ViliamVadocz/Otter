import os
import sys
import time
import cProfile
from pstats import Stats, SortKey
from shutil import rmtree
from pathlib import Path

from rlbot.agents.base_agent import SimpleControllerState
from rlbot.agents.standalone.standalone_bot import StandaloneBot, run_bot

from bot import Otter

PROFILE_DATA_DIR = (Path(__file__).parent / "profile_data").absolute()
COMBINED_FILE = PROFILE_DATA_DIR / "combined"
MAX_FRAMES = 10_000


class OtterProfileBot(Otter, StandaloneBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = 0

    def get_output(self, game_tick_packet):
        if self.frame >= MAX_FRAMES:
            print("Profiling done, interrupt this with Ctrl+C")
            return SimpleControllerState()
        pr = cProfile.Profile()
        pr.enable()
        output = super().get_output(game_tick_packet)
        pr.disable()
        pr.create_stats()
        pr.dump_stats(PROFILE_DATA_DIR / str(self.frame))
        self.frame += 1
        return output


if __name__ == "__main__":

    if os.path.isfile(COMBINED_FILE):
        ps = Stats()
        ps.add(str(COMBINED_FILE))
        ps.sort_stats(SortKey.TIME).print_stats()
        exit()

    if os.path.isdir(PROFILE_DATA_DIR):
        rmtree(PROFILE_DATA_DIR)
    os.mkdir(PROFILE_DATA_DIR)

    config_path = (Path(__file__).parent / "bot.cfg").absolute()
    sys.argv[1:] = [
        f"--config-file={config_path}",
        "--player-index=0",
        "--team=0",
        "--spawn-id=1",
    ]
    try:
        run_bot(OtterProfileBot)
    except Exception as err:
        print(err)

    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Combining frame profile data")
    print("Please wait, it might take a minute")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    ps = Stats()
    for file in os.listdir(PROFILE_DATA_DIR):
        path_to_file = PROFILE_DATA_DIR / file
        if os.path.isfile(path_to_file):
            ps.add(str(path_to_file))
            os.remove(path_to_file)
    ps.dump_stats(str(COMBINED_FILE))
    ps.sort_stats(SortKey.TIME).print_stats()
