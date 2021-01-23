from enum import Enum

from rlbot.messages.flat import MatchSettings


class GameMode(Enum):
    Soccer = 0
    Hoops = 1
    Dropshot = 2
    Hockey = 3
    Rumble = 4
    Heatseeker = 5


class Map(Enum):
    DFHStadium = 0
    Mannfield = 1
    ChampionsField = 2
    UrbanCentral = 3
    BeckwithPark = 4
    UtopiaColiseum = 5
    Wasteland = 6
    NeoTokyo = 7
    AquaDome = 8
    StarbaseArc = 9
    Farmstead = 10
    SaltyShores = 11
    DFHStadium_Stormy = 12
    DFHStadium_Day = 13
    Mannfield_Stormy = 14
    Mannfield_Night = 15
    ChampionsField_Day = 16
    BeckwithPark_Stormy = 17
    BeckwithPark_Midnight = 18
    UrbanCentral_Night = 19
    UrbanCentral_Dawn = 20
    UtopiaColiseum_Dusk = 21
    DFHStadium_Snowy = 22
    Mannfield_Snowy = 23
    UtopiaColiseum_Snowy = 24
    Badlands = 25
    Badlands_Night = 26
    TokyoUnderpass = 27
    Arctagon = 28
    Pillars = 29
    Cosmic = 30
    DoubleGoal = 31
    Octagon = 32
    Underpass = 33
    UtopiaRetro = 34
    Hoops_DunkHouse = 35
    DropShot_Core707 = 36
    ThrowbackStadium = 37
    ForbiddenTemple = 38
    RivalsArena = 39
    Farmstead_Night = 40
    SaltyShores_Night = 41
    NeonFields = 42


class ParsedMatchSettings:
    def __init__(self, match_settings: MatchSettings):
        self.game_mode = GameMode(match_settings.GameMode())
        self.map = Map(match_settings.GameMap())
        # TODO Add others when needed.
        # https://github.com/RLBot/RLBot/blob/master/src/main/flatbuffers/rlbot.fbs#L788
