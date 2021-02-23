from typing import List, Optional

from tmcp import TMCP_VERSION, ActionType
from tmcp import TMCPHandler as TMCPHandlerForBots
from tmcp import TMCPMessage
from rlbot.matchcomms.client import MatchcommsClient
from rlbot.agents.base_script import BaseScript
from rlbot.utils.structures.game_data_struct import GameTickPacket


class TMCPHandler(TMCPHandlerForBots):
    def __init__(self, matchcomms: MatchcommsClient):
        self.matchcomms: MatchcommsClient = matchcomms
        self.last_time = 0.0
        self.enabled = True

    def parse(self, message: dict) -> Optional[TMCPMessage]:
        # Ignore messages using a different version of the protocol.
        if message.get("tmcp_version") != TMCP_VERSION:
            return None
        # Don't filter by team.
        return TMCPMessage.from_dict(message)


class MyScript(BaseScript):
    def __init__(self):
        super().__init__("TMCP Tracker")
        self.tmcp_handler = TMCPHandler(self.matchcomms)

    def run(self):
        while True:
            packet: GameTickPacket = self.wait_game_tick_packet()
            new_messages: List[TMCPMessage] = self.tmcp_handler.recv()
            for message in new_messages:
                bot_name = packet.game_cars[message.index].name
                action_type: ActionType = message.action_type
                print(f"[{bot_name}]: {action_type}")


if __name__ == "__main__":
    script = MyScript()
    script.run()
