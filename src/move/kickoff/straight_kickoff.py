# fmt: off
from typing import Optional

from rlbot.agents.base_agent import SimpleControllerState


class StraightKickoff:
    def __init__(self):
        self.timer: float = 0.0
        self.finished: bool = False
        self.controls: Optional[SimpleControllerState] = None

    def step(self, dt: float):
        if self.timer == 0.0:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.00850820541381836:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.01750969886779785:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.026511669158935547:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.035514116287231445:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.04451584815979004:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.053839921951293945:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.06284117698669434:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.071746826171875:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.08103275299072266:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.09027767181396484:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.0989675521850586:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1074516773223877:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1164548397064209:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1254565715789795:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1346607208251953:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.14323115348815918:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.15248632431030273:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.16112256050109863:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.17012500762939453:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.17912650108337402:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.188215970993042:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.19691038131713867:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.20542669296264648:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.21442937850952148:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.22304248809814453:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.23204326629638672:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.24104595184326172:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2494211196899414:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.25785231590270996:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.26671695709228516:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2758791446685791:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.28466320037841797:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2934839725494385:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.30213427543640137:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3106398582458496:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3196420669555664:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3286447525024414:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3376462459564209:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.346649169921875:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3556499481201172:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3647348880767822:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3737361431121826:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3822438716888428:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.39124608039855957:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3997523784637451:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4087553024291992:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4177570343017578:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.42678236961364746:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.43578505516052246:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.44478678703308105:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.45378851890563965:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.46279168128967285:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.47179365158081055:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.48098301887512207:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.490293025970459:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.498981237411499:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5074892044067383:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5164909362792969:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5250062942504883:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.534001350402832:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5430045127868652:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5515139102935791:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5607514381408691:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5697529315948486:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5787546634674072:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5877571105957031:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5965421199798584:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6050541400909424:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6140961647033691:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6230981349945068:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6324899196624756:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6414940357208252:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6503543853759766:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6596457958221436:
            self.controls = SimpleControllerState(throttle=0.17253638803958893, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6680762767791748:
            self.controls = SimpleControllerState(throttle=0.23528245091438293, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6772651672363281:
            self.controls = SimpleControllerState(throttle=0.28234198689460754, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6862673759460449:
            self.controls = SimpleControllerState(throttle=0.35293129086494446, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6952688694000244:
            self.controls = SimpleControllerState(throttle=0.43136388063430786, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7043333053588867:
            self.controls = SimpleControllerState(throttle=0.47058016061782837, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7135446071624756:
            self.controls = SimpleControllerState(throttle=0.5058748126029968, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7228243350982666:
            self.controls = SimpleControllerState(throttle=0.5843073725700378, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7314748764038086:
            self.controls = SimpleControllerState(throttle=0.6274452805519104, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7404775619506836:
            self.controls = SimpleControllerState(throttle=0.6666615605354309, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7494783401489258:
            self.controls = SimpleControllerState(throttle=0.6862697005271912, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.758481502532959:
            self.controls = SimpleControllerState(throttle=0.7568590641021729, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7677712440490723:
            self.controls = SimpleControllerState(throttle=0.8313699960708618, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.77677321434021:
            self.controls = SimpleControllerState(throttle=0.9372539520263672, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7855360507965088:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7945396900177002:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8035421371459961:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8125438690185547:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8215453624725342:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8305480480194092:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8390085697174072:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.847834587097168:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8562722206115723:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.865447998046875:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8744499683380127:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8834519386291504:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.892453670501709:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9014556407928467:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9104576110839844:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9194595813751221:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9279654026031494:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9369676113128662:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9459693431854248:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9543118476867676:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.96358323097229:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9725852012634277:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9818265438079834:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9909660816192627:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9999682903289795:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0084779262542725:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0170621871948242:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0262842178344727:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0352880954742432:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0442907810211182:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0528082847595215:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0618114471435547:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0708141326904297:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0800745487213135:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0890758037567139:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.097837209701538:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.106839895248413:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1158409118652344:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1248438358306885:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1331772804260254:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1423442363739014:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1513464450836182:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1598522663116455:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1688547134399414:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1778569221496582:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1868581771850586:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1958603858947754:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2048921585083008:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.213468313217163:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.222752571105957:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2317593097686768:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2404861450195312:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2494909763336182:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.258493423461914:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2674944400787354:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2769196033477783:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2857484817504883:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.294754981994629:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.303757667541504:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3127593994140625:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3220441341400146:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3306207656860352:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3396995067596436:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.348762035369873:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.357116460800171:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3656418323516846:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3746445178985596:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3842809200286865:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3933031558990479:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.401810646057129:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4108119010925293:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.12155522406101227, pitch=0.0, yaw=0.12155522406101227, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.419814109802246:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.18430127203464508, pitch=0.0, yaw=0.18430127203464508, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4288160800933838:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.2470473349094391, pitch=0.0, yaw=0.2470473349094391, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4378197193145752:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.3333231508731842, pitch=0.0, yaw=0.3333231508731842, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.44681978225708:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.5058748126029968, pitch=0.0, yaw=0.5058748126029968, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4558219909667969:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.6313669085502625, pitch=0.0, yaw=0.6313669085502625, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4648237228393555:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.749015748500824, pitch=0.0, yaw=0.749015748500824, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4738261699676514:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9058809280395508, pitch=0.0, yaw=0.9058809280395508, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4830775260925293:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4915833473205566:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5001320838928223:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5086426734924316:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5177669525146484:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5267407894134521:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5357427597045898:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5447442531585693:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5537464618682861:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5627481937408447:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5717508792877197:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9921567440032959, pitch=0.0, yaw=0.0, roll=0.9921567440032959, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5807526111602783:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.8980376720428467, pitch=0.0, yaw=0.0, roll=0.8980376720428467, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5897600650787354:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.7333292365074158, pitch=0.0, yaw=0.0, roll=0.7333292365074158, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.599073886871338:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.4039124846458435, pitch=-0.19217506051063538, yaw=0.0, roll=0.4039124846458435, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6080756187438965:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-0.20786157250404358, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.616581678390503:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-0.20786157250404358, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6255853176116943:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2706076204776764, pitch=-0.2784508764743805, yaw=0.0, roll=-0.2706076204776764, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.634587049484253:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6235541701316833, pitch=-0.4902188181877136, yaw=0.0, roll=-0.6235541701316833, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.643589735031128:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8588519096374512, pitch=-0.6157109141349792, yaw=0.0, roll=-0.8588519096374512, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.652890920639038:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8823816776275635, pitch=-0.6078676581382751, yaw=0.0, roll=-0.8823816776275635, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6618928909301758:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8902249336242676, pitch=-0.5921811461448669, yaw=0.0, roll=-0.8902249336242676, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6708953380584717:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8980681896209717, pitch=-0.5372783541679382, yaw=0.0, roll=-0.8980681896209717, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6798973083496094:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9059114456176758, pitch=-0.5137485861778259, yaw=0.0, roll=-0.9059114456176758, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6888988018035889:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9294412136077881, pitch=-0.4510025382041931, yaw=0.0, roll=-0.9294412136077881, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6979010105133057:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9372844696044922, pitch=-0.4274727702140808, yaw=0.0, roll=-0.9372844696044922, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7069029808044434:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9608142375946045, pitch=-0.3882564902305603, yaw=0.0, roll=-0.9608142375946045, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7159051895141602:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9765007495880127, pitch=-0.3333536684513092, yaw=0.0, roll=-0.9765007495880127, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7250609397888184:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.3098239004611969, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.734062910079956:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.2627643644809723, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.742572546005249:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.23923459649085999, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7515735626220703:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.21570482850074768, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7605698108673096:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.17648853361606598, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7695715427398682:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.12942899763584137, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7780768871307373:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7870819568634033:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.796083927154541:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.8045921325683594:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.813594102859497:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.8225955963134766:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.12939848005771637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8315980434417725:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.22351756691932678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8406007289886475:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.23136082291603088, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8496019840240479:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2548905909061432, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8585774898529053:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.867579698562622:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=0.3411664068698883, yaw=0.0, roll=-0.9921872615814209, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8765811920166016:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9686574935913086, pitch=0.3568529188632965, yaw=0.0, roll=-0.9686574935913086, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.885169267654419:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9608142375946045, pitch=0.3803827166557312, yaw=0.0, roll=-0.9608142375946045, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8936822414398193:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9451277256011963, pitch=0.4274422526359558, yaw=0.0, roll=-0.9451277256011963, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9026849269866943:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9137547016143799, pitch=0.4509720206260681, yaw=0.0, roll=-0.9137547016143799, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.911686897277832:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8980681896209717, pitch=0.4823450446128845, yaw=0.0, roll=-0.8980681896209717, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9206886291503906:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8902249336242676, pitch=0.5607776045799255, yaw=0.0, roll=-0.8902249336242676, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9296901226043701:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8666951656341553, pitch=0.5921506285667419, yaw=0.0, roll=-0.8666951656341553, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.938692331314087:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.843165397644043, pitch=0.6392101645469666, yaw=0.0, roll=-0.843165397644043, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.947502613067627:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8274788856506348, pitch=0.6627399325370789, yaw=0.0, roll=-0.8274788856506348, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9566967487335205:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8039491176605225, pitch=0.6784264445304871, yaw=0.0, roll=-0.8039491176605225, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.965698003768921:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7882626056671143, pitch=0.6941129565238953, yaw=0.0, roll=-0.7882626056671143, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.974700689315796:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.764732837677002, pitch=0.7097994685173035, yaw=0.0, roll=-0.764732837677002, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9837024211883545:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7412030100822449, pitch=0.7333292365074158, yaw=0.0, roll=-0.7412030100822449, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9927048683166504:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7255164980888367, pitch=0.7411724925041199, yaw=0.0, roll=-0.7255164980888367, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.001707077026367:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7255164980888367, pitch=0.7411724925041199, yaw=0.0, roll=-0.7255164980888367, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0107083320617676:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7255164980888367, pitch=0.749015748500824, yaw=0.0, roll=-0.7255164980888367, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.019808292388916:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7333597540855408, pitch=0.749015748500824, yaw=0.0, roll=-0.7333597540855408, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0288095474243164:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7255164980888367, pitch=0.7411724925041199, yaw=0.0, roll=-0.7255164980888367, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.037811517715454:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7333597540855408, pitch=0.7411724925041199, yaw=0.0, roll=-0.7333597540855408, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.04681396484375:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7333597540855408, pitch=0.7411724925041199, yaw=0.0, roll=-0.7333597540855408, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.055823802947998:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7333597540855408, pitch=0.7411724925041199, yaw=0.0, roll=-0.7333597540855408, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.064826011657715:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7333597540855408, pitch=0.7411724925041199, yaw=0.0, roll=-0.7333597540855408, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0738282203674316:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7490463256835938, pitch=0.7411724925041199, yaw=0.0, roll=-0.7490463256835938, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.082829713821411:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8039491176605225, pitch=0.6941129565238953, yaw=0.0, roll=-0.8039491176605225, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0913333892822266:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8353221416473389, pitch=0.6627399325370789, yaw=0.0, roll=-0.8353221416473389, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0999350547790527:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8666951656341553, pitch=0.6078371405601501, yaw=0.0, roll=-0.8666951656341553, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1084423065185547:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8980681896209717, pitch=0.5058748126029968, yaw=0.0, roll=-0.8980681896209717, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1174447536468506:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9372844696044922, pitch=0.4352855086326599, yaw=0.0, roll=-0.9372844696044922, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.126446485519409:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9608142375946045, pitch=0.3803827166557312, yaw=0.0, roll=-0.9608142375946045, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.135448694229126:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9765007495880127, pitch=0.3490096628665924, yaw=0.0, roll=-0.9765007495880127, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.144451141357422:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=0.3254798948764801, yaw=0.0, roll=-0.9921872615814209, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1535580158233643:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3097933828830719, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.162559747695923:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1715612411499023:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.180563449859619:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.189565896987915:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.197913885116577:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2069151401519775:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.215916872024536:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.224395513534546:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2330973148345947:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2423596382141113:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3019501268863678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.251549005508423:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2605514526367188:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.269615411758423:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.278505325317383:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2875075340270996:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2965095043182373:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.305511236190796:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.3138773441314697:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.322878837585449:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.2941068708896637, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.331881046295166:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3097933828830719, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.3408827781677246:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3254798948764801, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.3498849868774414:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.3490096628665924, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.358886480331421:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9686574935913086, pitch=0.3646961748600006, yaw=0.0, roll=-0.9686574935913086, jump=False, boost=False, handbrake=True)
        elif self.timer <= 2.3678901195526123:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9608142375946045, pitch=0.3803827166557312, yaw=-0.9608142375946045, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3768908977508545:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=-0.9451277256011963, pitch=0.4352855086326599, yaw=-0.9451277256011963, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.385892391204834:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=-0.9372844696044922, pitch=0.4509720206260681, yaw=-0.9372844696044922, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.39489483833313:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=-0.9137547016143799, pitch=0.4745017886161804, yaw=-0.9137547016143799, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4038968086242676:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.9059114456176758, pitch=0.4980315566062927, yaw=-0.9059114456176758, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.412902593612671:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8980681896209717, pitch=0.521561324596405, yaw=-0.8980681896209717, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4219110012054443:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5372478365898132, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.430912971496582:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5529343485832214, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.440031051635742:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4484763145446777:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.457122564315796:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4661264419555664:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5607776045799255, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.475128412246704:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4841315746307373:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4934566020965576:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5024585723876953:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.511460304260254:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5204625129699707:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.528883934020996:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.537886619567871:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5686208605766296, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.546889305114746:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5607776045799255, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5558903217315674:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.5529343485832214, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.564314126968384:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8980681896209717, pitch=0.5372478365898132, yaw=-0.8980681896209717, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5727293491363525:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8902249336242676, pitch=0.4980315566062927, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5817322731018066:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.8510086536407471, pitch=0.4823450446128845, yaw=-0.8510086536407471, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.590733766555786:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.6941434741020203, pitch=0.443128764629364, yaw=-0.6941434741020203, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.599735736846924:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.5294350981712341, pitch=0.4117557406425476, yaw=-0.5294350981712341, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.608738660812378:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.3411969244480133, pitch=0.3646961748600006, yaw=-0.3411969244480133, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.61781907081604:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.12158574163913727, pitch=0.3333231508731842, yaw=-0.12158574163913727, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6271016597747803:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.0, pitch=0.13724173605442047, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.636104106903076:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6451058387756348:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6541762351989746:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6629083156585693:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.12155522406101227, pitch=0.0, yaw=0.12155522406101227, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6719086170196533:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.12155522406101227, pitch=0.0, yaw=0.12155522406101227, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.680912971496582:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.12155522406101227, pitch=0.0, yaw=0.12155522406101227, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.689960241317749:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.11371196806430817, pitch=0.0, yaw=0.11371196806430817, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.698962688446045:
            self.controls = SimpleControllerState(throttle=0.9725486040115356, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7075002193450928:
            self.controls = SimpleControllerState(throttle=0.9686269760131836, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7165467739105225:
            self.controls = SimpleControllerState(throttle=0.9647053480148315, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.725548028945923:
            self.controls = SimpleControllerState(throttle=0.9450972080230713, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7345497608184814:
            self.controls = SimpleControllerState(throttle=0.9098025560379028, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.74355149269104:
            self.controls = SimpleControllerState(throttle=0.8901944160461426, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7525572776794434:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7610645294189453:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7697126865386963:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7787106037139893:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.787712335586548:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.796358108520508:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.804971694946289:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8136467933654785:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8227596282958984:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8317947387695312:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8408279418945312:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.849830150604248:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.858832359313965:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.867833375930786:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.876835823059082:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8863296508789062:
            self.controls = SimpleControllerState(throttle=0.8666646480560303, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.8953731060028076:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.904374599456787:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.9128644466400146:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.9218204021453857:
            self.controls = SimpleControllerState(throttle=0.8548997640609741, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.93080997467041:
            self.controls = SimpleControllerState(throttle=0.8509781360626221, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.939812183380127:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.9490740299224854:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.958204507827759:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.96671199798584:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.975706100463867:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.984707832336426:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.9937100410461426:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.002711772918701:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.0122013092041016:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.0212061405181885:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.030214309692383:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.0385656356811523:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.0470433235168457:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=0.16861476004123688, pitch=0.0, yaw=0.16861476004123688, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 3.0562422275543213:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.2627338469028473, pitch=-0.16080202162265778, yaw=0.2627338469028473, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 3.0652453899383545:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.4195989966392517, pitch=-0.23923459649085999, yaw=0.4195989966392517, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 3.0737524032592773:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.5921506285667419, pitch=-0.3490401804447174, yaw=0.5921506285667419, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 3.0829598903656006:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.5372783541679382, yaw=0.9137241840362549, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 3.09211802482605:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9372539520263672, pitch=-0.5686513781547546, yaw=0.0, roll=0.9372539520263672, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.100626230239868:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9372539520263672, pitch=-0.5843378901481628, yaw=0.0, roll=0.9372539520263672, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.109628438949585:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.921567440032959, pitch=-0.600024402141571, yaw=0.0, roll=0.921567440032959, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.1186301708221436:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6157109141349792, yaw=0.0, roll=0.9137241840362549, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.1276321411132812:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6235541701316833, yaw=0.0, roll=0.9137241840362549, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.136634588241577:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6235541701316833, yaw=0.0, roll=0.9137241840362549, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.145228862762451:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6313974261283875, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.15374493598938:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6313974261283875, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.162752151489258:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6313974261283875, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.171186923980713:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6313974261283875, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1801884174346924:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6313974261283875, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.18869686126709:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.6235541701316833, yaw=0.0, roll=0.9137241840362549, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1976993083953857:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9607837200164795, pitch=-0.5608081221580505, yaw=0.0, roll=0.9607837200164795, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.206700563430786:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9843134880065918, pitch=-0.4666890501976013, yaw=0.0, roll=0.9843134880065918, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.215782642364502:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3255104124546051, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.22479248046875:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2627643644809723, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.2337934970855713:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.20001831650733948, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.242795944213867:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.2512128353118896:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.260309934616089:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.2688186168670654:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.277820348739624:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.286823034286499:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.2961277961730957:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.305131435394287:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.314131736755371:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.3226406574249268:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.13724173605442047, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.3316421508789062:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.14508499205112457, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.340644598007202:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.14508499205112457, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3496463298797607:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.15292824804782867, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3586480617523193:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.15292824804782867, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.367650270462036:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.15292824804782867, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3766534328460693:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.16077150404453278, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.385031223297119:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.17645801603794098, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.394026279449463:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.19998779892921448, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.403029203414917:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4120302200317383:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4204485416412354:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4294514656066895:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4387564659118652:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.447758436203003:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4567604064941406:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.465762138366699:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.474763870239258:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.483252763748169:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.19998779892921448, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.4915876388549805:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.19998779892921448, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.500589370727539:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.17645801603794098, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.509096384048462:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.16077150404453278, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.5174529552459717:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.14508499205112457, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.525960922241211:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.14508499205112457, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.5349628925323486:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.10586871206760406, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5439653396606445:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5523734092712402:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.560880661010742:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.5698819160461426:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.5788843631744385:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.5875699520111084:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5965752601623535:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.605010986328125:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6142425537109375:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6235313415527344:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.17648853361606598, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.632533073425293:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.20001831650733948, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.641535758972168:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.22354808449745178, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6505374908447266:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2470778524875641, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6595396995544434:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2784508764743805, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6685409545898438:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2862941324710846, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.6776201725006104:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3098239004611969, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.686682939529419:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3255104124546051, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.695686101913452:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3255104124546051, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7046866416931152:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3333536684513092, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.713698387145996:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3333536684513092, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7229902744293213:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3647266924381256, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.731497049331665:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3804132342338562, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7404990196228027:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7495789527893066:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7585806846618652:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.767583131790161:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7765848636627197:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.7855865955352783:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.794589042663574:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.803439140319824:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.8125360012054443:
            self.controls = SimpleControllerState(throttle=0.9725486040115356, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.821537971496582:
            self.controls = SimpleControllerState(throttle=0.9686269760131836, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.830540180206299:
            self.controls = SimpleControllerState(throttle=0.9647053480148315, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.8395419120788574:
            self.controls = SimpleControllerState(throttle=0.9176458120346069, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.8485443592071533:
            self.controls = SimpleControllerState(throttle=0.8980376720428467, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.857546329498291:
            self.controls = SimpleControllerState(throttle=0.8901944160461426, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.86659836769104:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.8757095336914062:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.884714365005493:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.893717050552368:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.902719736099243:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.9116158485412598:
            self.controls = SimpleControllerState(throttle=0.8666646480560303, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.920961856842041:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.9294722080230713:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.9921567440032959, pitch=-0.3882564902305603, yaw=0.0, roll=0.9921567440032959, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.937833547592163:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.9764702320098877, pitch=-0.3882564902305603, yaw=0.0, roll=0.9764702320098877, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.9464476108551025:
            self.controls = SimpleControllerState(throttle=0.8548997640609741, steer=0.9686269760131836, pitch=-0.3882564902305603, yaw=0.0, roll=0.9686269760131836, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.9554524421691895:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.9450972080230713, pitch=-0.3882564902305603, yaw=0.9450972080230713, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9644858837127686:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.9294106960296631, pitch=-0.3804132342338562, yaw=0.9294106960296631, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.972892999649048:
            self.controls = SimpleControllerState(throttle=0.8392132520675659, steer=0.9137241840362549, pitch=-0.3490401804447174, yaw=0.9137241840362549, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.981274127960205:
            self.controls = SimpleControllerState(throttle=0.8352916240692139, steer=0.8980376720428467, pitch=-0.3255104124546051, yaw=0.8980376720428467, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.990100145339966:
            self.controls = SimpleControllerState(throttle=0.8313699960708618, steer=0.843134880065918, pitch=-0.317667156457901, yaw=0.843134880065918, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9991018772125244:
            self.controls = SimpleControllerState(throttle=0.8196051120758057, steer=0.7882320880889893, pitch=-0.2941373884677887, yaw=0.7882320880889893, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.008105278015137:
            self.controls = SimpleControllerState(throttle=0.8117618560791016, steer=0.764702320098877, pitch=-0.2706076204776764, yaw=0.764702320098877, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.017231464385986:
            self.controls = SimpleControllerState(throttle=0.8039186000823975, steer=0.7254859805107117, pitch=-0.2549211084842682, yaw=0.7254859805107117, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.026233673095703:
            self.controls = SimpleControllerState(throttle=0.768623948097229, steer=0.7097994685173035, pitch=-0.23923459649085999, yaw=0.7097994685173035, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0347418785095215:
            self.controls = SimpleControllerState(throttle=0.7294076085090637, steer=0.6941129565238953, pitch=-0.22354808449745178, yaw=0.6941129565238953, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.043744087219238:
            self.controls = SimpleControllerState(throttle=0.6666615605354309, steer=0.6862697005271912, pitch=-0.22354808449745178, yaw=0.6862697005271912, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.052745819091797:
            self.controls = SimpleControllerState(throttle=0.6352885365486145, steer=0.6784264445304871, pitch=-0.22354808449745178, yaw=0.6784264445304871, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0617475509643555:
            self.controls = SimpleControllerState(throttle=0.5921506285667419, steer=0.6784264445304871, pitch=-0.22354808449745178, yaw=0.6784264445304871, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.070870637893677:
            self.controls = SimpleControllerState(throttle=0.5568559765815735, steer=0.6784264445304871, pitch=-0.21570482850074768, yaw=0.6784264445304871, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.079418182373047:
            self.controls = SimpleControllerState(throttle=0.5372478365898132, steer=0.6784264445304871, pitch=-0.21570482850074768, yaw=0.6784264445304871, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.087877988815308:
            self.controls = SimpleControllerState(throttle=0.5137180685997009, steer=0.6862697005271912, pitch=-0.21570482850074768, yaw=0.6862697005271912, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.096639156341553:
            self.controls = SimpleControllerState(throttle=0.4862666726112366, steer=0.7097994685173035, pitch=-0.21570482850074768, yaw=0.7097994685173035, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.105731964111328:
            self.controls = SimpleControllerState(throttle=0.4666585326194763, steer=0.7411724925041199, pitch=-0.22354808449745178, yaw=0.7411724925041199, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.1144633293151855:
            self.controls = SimpleControllerState(throttle=0.4509720206260681, steer=0.7960753440856934, pitch=-0.21570482850074768, yaw=0.7960753440856934, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.123504400253296:
            self.controls = SimpleControllerState(throttle=0.4274422526359558, steer=0.8980376720428467, pitch=-0.22354808449745178, yaw=0.8980376720428467, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.132506847381592:
            self.controls = SimpleControllerState(throttle=0.40783411264419556, steer=0.9294106960296631, pitch=-0.21570482850074768, yaw=0.9294106960296631, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.141510725021362:
            self.controls = SimpleControllerState(throttle=0.3803827166557312, steer=0.9764702320098877, pitch=-0.21570482850074768, yaw=0.9764702320098877, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.150511264801025:
            self.controls = SimpleControllerState(throttle=0.3568529188632965, steer=0.9921567440032959, pitch=-0.21570482850074768, yaw=0.9921567440032959, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.159512758255005:
            self.controls = SimpleControllerState(throttle=0.32155826687812805, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.168759346008301:
            self.controls = SimpleControllerState(throttle=0.29802849888801575, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.177763938903809:
            self.controls = SimpleControllerState(throttle=0.27449873089790344, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.186651229858398:
            self.controls = SimpleControllerState(throttle=0.26665547490119934, steer=1.0, pitch=-0.21570482850074768, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.195472240447998:
            self.controls = SimpleControllerState(throttle=0.2548905909061432, steer=1.0, pitch=-0.21570482850074768, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.204477548599243:
            self.controls = SimpleControllerState(throttle=0.24312570691108704, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.213013648986816:
            self.controls = SimpleControllerState(throttle=0.23920407891273499, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.222061395645142:
            self.controls = SimpleControllerState(throttle=0.23528245091438293, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.2310638427734375:
            self.controls = SimpleControllerState(throttle=0.23136082291603088, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.240065574645996:
            self.controls = SimpleControllerState(throttle=0.23136082291603088, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.249067544937134:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=1.0, pitch=-0.21570482850074768, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.257841110229492:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=1.0, pitch=-0.21570482850074768, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.266843795776367:
            self.controls = SimpleControllerState(throttle=0.22743919491767883, steer=1.0, pitch=-0.22354808449745178, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.2758448123931885:
            self.controls = SimpleControllerState(throttle=0.22743919491767883, steer=1.0, pitch=-0.21570482850074768, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.284877061843872:
            self.controls = SimpleControllerState(throttle=0.21959593892097473, steer=1.0, pitch=-0.20786157250404358, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.293878793716431:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=1.0, pitch=-0.20001831650733948, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.302881479263306:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.9764702320098877, pitch=-0.19217506051063538, yaw=0.9764702320098877, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.311882734298706:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.9529404640197754, pitch=-0.19217506051063538, yaw=0.9529404640197754, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.320884943008423:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.9137241840362549, pitch=-0.17648853361606598, yaw=0.9137241840362549, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.3298869132995605:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.8901944160461426, pitch=-0.16080202162265778, yaw=0.8901944160461426, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.338890075683594:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.8274483680725098, pitch=-0.15295876562595367, yaw=0.8274483680725098, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.3476433753967285:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.8039186000823975, pitch=-0.14511550962924957, yaw=0.8039186000823975, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.356647968292236:
            self.controls = SimpleControllerState(throttle=0.21567431092262268, steer=0.7960753440856934, pitch=-0.13727225363254547, yaw=0.7960753440856934, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.365650415420532:
            self.controls = SimpleControllerState(throttle=0.21959593892097473, steer=0.7882320880889893, pitch=-0.13727225363254547, yaw=0.7882320880889893, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.374652862548828:
            self.controls = SimpleControllerState(throttle=0.22743919491767883, steer=0.7803888320922852, pitch=-0.13727225363254547, yaw=0.7803888320922852, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.383828163146973:
            self.controls = SimpleControllerState(throttle=0.22743919491767883, steer=0.772545576095581, pitch=-0.13727225363254547, yaw=0.772545576095581, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.3928327560424805:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.7803888320922852, pitch=-0.13727225363254547, yaw=0.7803888320922852, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.401339054107666:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.7882320880889893, pitch=-0.13727225363254547, yaw=0.7882320880889893, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.410342216491699:
            self.controls = SimpleControllerState(throttle=0.22743919491767883, steer=0.7882320880889893, pitch=-0.13727225363254547, yaw=0.7882320880889893, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.419536590576172:
            self.controls = SimpleControllerState(throttle=0.2470473349094391, steer=0.7803888320922852, pitch=-0.13727225363254547, yaw=0.7803888320922852, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.428066968917847:
            self.controls = SimpleControllerState(throttle=0.26665547490119934, steer=0.772545576095581, pitch=-0.13727225363254547, yaw=0.772545576095581, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.437070846557617:
            self.controls = SimpleControllerState(throttle=0.28234198689460754, steer=0.764702320098877, pitch=-0.13727225363254547, yaw=0.764702320098877, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.446073293685913:
            self.controls = SimpleControllerState(throttle=0.30587175488471985, steer=0.7411724925041199, pitch=-0.13727225363254547, yaw=0.7411724925041199, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.455075740814209:
            self.controls = SimpleControllerState(throttle=0.3333231508731842, steer=0.6941129565238953, pitch=-0.13727225363254547, yaw=0.6941129565238953, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.464079856872559:
            self.controls = SimpleControllerState(throttle=0.35293129086494446, steer=0.670583188533783, pitch=-0.13727225363254547, yaw=0.670583188533783, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.473336219787598:
            self.controls = SimpleControllerState(throttle=0.3725394308567047, steer=0.6392101645469666, pitch=-0.13727225363254547, yaw=0.6392101645469666, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.482498645782471:
            self.controls = SimpleControllerState(throttle=0.3960692286491394, steer=0.6235236525535583, pitch=-0.13727225363254547, yaw=0.6235236525535583, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.491711854934692:
            self.controls = SimpleControllerState(throttle=0.4274422526359558, steer=0.5921506285667419, pitch=-0.13727225363254547, yaw=0.5921506285667419, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.501203775405884:
            self.controls = SimpleControllerState(throttle=0.44705039262771606, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.510447263717651:
            self.controls = SimpleControllerState(throttle=0.47058016061782837, steer=0.5921506285667419, pitch=-0.13727225363254547, yaw=0.5921506285667419, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.519643068313599:
            self.controls = SimpleControllerState(throttle=0.5019531846046448, steer=0.5921506285667419, pitch=-0.13727225363254547, yaw=0.5921506285667419, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.528713226318359:
            self.controls = SimpleControllerState(throttle=0.517639696598053, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.538177251815796:
            self.controls = SimpleControllerState(throttle=0.5372478365898132, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.547292947769165:
            self.controls = SimpleControllerState(throttle=0.5646992325782776, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.556430816650391:
            self.controls = SimpleControllerState(throttle=0.5882290005683899, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.565432548522949:
            self.controls = SimpleControllerState(throttle=0.599993884563446, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.574434995651245:
            self.controls = SimpleControllerState(throttle=0.6039155125617981, steer=0.5921506285667419, pitch=-0.13727225363254547, yaw=0.5921506285667419, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.583559989929199:
            self.controls = SimpleControllerState(throttle=0.6078371405601501, steer=0.5921506285667419, pitch=-0.13727225363254547, yaw=0.5921506285667419, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.59256649017334:
            self.controls = SimpleControllerState(throttle=0.6117587685585022, steer=0.5843073725700378, pitch=-0.13727225363254547, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.601568222045898:
            self.controls = SimpleControllerState(throttle=0.6117587685585022, steer=0.5843073725700378, pitch=-0.14511550962924957, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.610570192337036:
            self.controls = SimpleControllerState(throttle=0.6117587685585022, steer=0.5764641165733337, pitch=-0.14511550962924957, yaw=0.5764641165733337, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.619888544082642:
            self.controls = SimpleControllerState(throttle=0.6078371405601501, steer=0.5372478365898132, pitch=-0.13727225363254547, yaw=0.5372478365898132, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.628890514373779:
            self.controls = SimpleControllerState(throttle=0.6039155125617981, steer=0.4509720206260681, pitch=-0.13727225363254547, yaw=0.4509720206260681, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.637893199920654:
            self.controls = SimpleControllerState(throttle=0.599993884563446, steer=0.4039124846458435, pitch=-0.14511550962924957, yaw=0.4039124846458435, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.646407127380371:
            self.controls = SimpleControllerState(throttle=0.5764641165733337, steer=0.317636638879776, pitch=-0.14511550962924957, yaw=0.317636638879776, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.655145883560181:
            self.controls = SimpleControllerState(throttle=0.5372478365898132, steer=0.20783105492591858, pitch=-0.14511550962924957, yaw=0.20783105492591858, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.663502931594849:
            self.controls = SimpleControllerState(throttle=0.5137180685997009, steer=0.12939848005771637, pitch=-0.14511550962924957, yaw=0.12939848005771637, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.672290802001953:
            self.controls = SimpleControllerState(throttle=0.47842341661453247, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.681586980819702:
            self.controls = SimpleControllerState(throttle=0.42352062463760376, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.690629720687866:
            self.controls = SimpleControllerState(throttle=0.36861780285835266, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.699631690979004:
            self.controls = SimpleControllerState(throttle=0.2627338469028473, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.708721399307251:
            self.controls = SimpleControllerState(throttle=0.20783105492591858, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.717106342315674:
            self.controls = SimpleControllerState(throttle=0.10979034006595612, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.726398468017578:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.7350852489471436:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.743810653686523:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.752988815307617:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.76146936416626:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.7704713344573975:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.779476642608643:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.788668870925903:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.798066854476929:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.806495666503906:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.814992189407349:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.823507308959961:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.8320701122283936:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.841072082519531:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.849921464920044:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.858556270599365:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.8676838874816895:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.876686096191406:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.885688066482544:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.89469313621521:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.903334856033325:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.91231632232666:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.920707941055298:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.929707288742065:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.938710927963257:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.947713375091553:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.956715106964111:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.965717315673828:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.975045204162598:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        else:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
            self.finished = self.timer > 4.983932971954346

        self.timer += dt
