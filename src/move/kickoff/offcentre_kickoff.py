# flake8: noqa
# fmt: off
from typing import Optional

from rlbot.agents.base_agent import SimpleControllerState


class OffCentreKickoff:
    def __init__(self):
        self.timer: float = 0.0
        self.finished: bool = False
        self.controls: Optional[SimpleControllerState] = None

    def step(self, dt: float):
        if self.timer == 0.0:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.009001970291137695:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.018004655838012695:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.027005672454833984:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.03600811958312988:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.04538726806640625:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.054392099380493164:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.06319999694824219:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.07234382629394531:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.08166217803955078:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.090667724609375:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.0996696949005127:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1086721420288086:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.11702704429626465:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.12656021118164062:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1357100009918213:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.14472746849060059:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.15384435653686523:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.16257309913635254:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.17156577110290527:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.18056845664978027:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1895735263824463:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.19833731651306152:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2075943946838379:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.21664953231811523:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.22565150260925293:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.23465347290039062:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.24365758895874023:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.25291943550109863:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.26166296005249023:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2706775665283203:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2796785831451416:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2886815071105957:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.29708051681518555:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.30608224868774414:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.31508398056030273:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3240854740142822:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.33308887481689453:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3420901298522949:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3513646125793457:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.36041784286499023:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3696784973144531:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3789222240447998:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3879282474517822:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.39649510383605957:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4050109386444092:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4140164852142334:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4232218265533447:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4315640926361084:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.44078969955444336:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4499480724334717:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.45922207832336426:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4684021472930908:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4767770767211914:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.48607325553894043:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.49538230895996094:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5043847560882568:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5133860111236572:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5227138996124268:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5317225456237793:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5407295227050781:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5495171546936035:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5585694313049316:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5675716400146484:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5759212970733643:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5845608711242676:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5930132865905762:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6023464202880859:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6116397380828857:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6206440925598145:
            self.controls = SimpleControllerState(throttle=0.17645801603794098, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6299550533294678:
            self.controls = SimpleControllerState(throttle=0.23920407891273499, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6389567852020264:
            self.controls = SimpleControllerState(throttle=0.31371501088142395, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6479592323303223:
            self.controls = SimpleControllerState(throttle=0.3568529188632965, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6563920974731445:
            self.controls = SimpleControllerState(throttle=0.40783411264419556, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6653971672058105:
            self.controls = SimpleControllerState(throttle=0.44705039262771606, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6744744777679443:
            self.controls = SimpleControllerState(throttle=0.4980315566062927, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6829202175140381:
            self.controls = SimpleControllerState(throttle=0.5372478365898132, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6919312477111816:
            self.controls = SimpleControllerState(throttle=0.5882290005683899, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7009336948394775:
            self.controls = SimpleControllerState(throttle=0.6196020245552063, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7096540927886963:
            self.controls = SimpleControllerState(throttle=0.6392101645469666, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7181718349456787:
            self.controls = SimpleControllerState(throttle=0.6784264445304871, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7274858951568604:
            self.controls = SimpleControllerState(throttle=0.7058778405189514, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7364869117736816:
            self.controls = SimpleControllerState(throttle=0.7215643525123596, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7455344200134277:
            self.controls = SimpleControllerState(throttle=0.7254859805107117, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7545351982116699:
            self.controls = SimpleControllerState(throttle=0.7333292365074158, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7635376453399658:
            self.controls = SimpleControllerState(throttle=0.7333292365074158, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7727921009063721:
            self.controls = SimpleControllerState(throttle=0.7372508645057678, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7812762260437012:
            self.controls = SimpleControllerState(throttle=0.7372508645057678, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7902779579162598:
            self.controls = SimpleControllerState(throttle=0.7411724925041199, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.7992799282073975:
            self.controls = SimpleControllerState(throttle=0.772545576095581, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8077471256256104:
            self.controls = SimpleControllerState(throttle=0.8156834840774536, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8164973258972168:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8254985809326172:
            self.controls = SimpleControllerState(throttle=0.925489068031311, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8345010280609131:
            self.controls = SimpleControllerState(throttle=0.9568620920181274, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8435044288635254:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8525063991546631:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8615086078643799:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8705103397369385:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8802380561828613:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8897011280059814:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=-0.13727225363254547, pitch=0.0, yaw=-0.13727225363254547, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.8988142013549805:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2627643644809723, pitch=0.0, yaw=-0.2627643644809723, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9073097705841064:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.3333536684513092, pitch=0.0, yaw=-0.3333536684513092, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9161727428436279:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4117862582206726, pitch=0.0, yaw=-0.4117862582206726, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9246354103088379:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4980620741844177, pitch=0.0, yaw=-0.4980620741844177, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.93392014503479:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5686513781547546, pitch=0.0, yaw=-0.5686513781547546, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9427125453948975:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6863002181053162, pitch=0.0, yaw=-0.6863002181053162, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9514644145965576:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7490463256835938, pitch=0.0, yaw=-0.7490463256835938, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.959906816482544:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8039491176605225, pitch=-0.10589922964572906, yaw=-0.8039491176605225, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9692120552062988:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8353221416473389, pitch=-0.14511550962924957, yaw=-0.8353221416473389, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9775612354278564:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.843165397644043, pitch=-0.16080202162265778, yaw=-0.843165397644043, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9862017631530762:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.843165397644043, pitch=-0.19217506051063538, yaw=-0.843165397644043, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9955155849456787:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8353221416473389, pitch=-0.20786157250404358, yaw=-0.8353221416473389, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0045790672302246:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7568895816802979, pitch=-0.22354808449745178, yaw=-0.7568895816802979, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0133283138275146:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6863002181053162, pitch=-0.23923459649085999, yaw=-0.6863002181053162, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0224816799163818:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5529648661613464, pitch=-0.23923459649085999, yaw=-0.5529648661613464, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.031280279159546:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4353160262107849, pitch=-0.2470778524875641, yaw=-0.4353160262107849, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.040395736694336:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2706076204776764, pitch=-0.21570482850074768, yaw=-0.2706076204776764, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0493991374969482:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0584015846252441:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0674645900726318:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0760118961334229:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0847251415252686:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0931997299194336:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1017415523529053:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1107227802276611:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1193153858184814:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1284475326538086:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1367859840393066:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.145268440246582:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1547207832336426:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1631312370300293:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1717157363891602:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1802291870117188:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1892318725585938:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1982331275939941:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2073297500610352:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.216616153717041:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.224991798400879:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2339191436767578:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2424814701080322:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2508282661437988:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.259526252746582:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2685298919677734:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2771737575531006:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2865583896636963:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.295680046081543:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.304076910018921:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3131139278411865:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3215250968933105:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3300282955169678:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3385350704193115:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.13727225363254547, pitch=0.0, yaw=-0.13727225363254547, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3469178676605225:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2862941324710846, pitch=0.0, yaw=-0.2862941324710846, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3565583229064941:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4196295142173767, pitch=0.0, yaw=-0.4196295142173767, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.364973783493042:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5529648661613464, pitch=0.0, yaw=-0.5529648661613464, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3740344047546387:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6863002181053162, pitch=0.0, yaw=-0.6863002181053162, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3830368518829346:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8510086536407471, pitch=0.0, yaw=-0.8510086536407471, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3920767307281494:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9137547016143799, pitch=0.0, yaw=-0.9137547016143799, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.401078701019287:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.409621238708496:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4181342124938965:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4271540641784668:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4363415241241455:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.445108413696289:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4541099071502686:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4631125926971436:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8902249336242676, pitch=0.0, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.472287893295288:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7804193496704102, pitch=0.0, yaw=-0.7804193496704102, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.480966567993164:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6235541701316833, pitch=0.0, yaw=-0.6235541701316833, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.4895377159118652:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4117862582206726, pitch=0.0, yaw=-0.4117862582206726, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.4983916282653809:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5073964595794678:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.3254798948764801, pitch=-0.16864527761936188, yaw=0.3254798948764801, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5159211158752441:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.6784264445304871, pitch=-0.2784508764743805, yaw=0.6784264445304871, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5251867771148682:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.317667156457901, yaw=1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5336918830871582:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.317667156457901, yaw=1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5429573059082031:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3098239004611969, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.5519590377807617:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.23923459649085999, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.5609619617462158:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.19217506051063538, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.5699632167816162:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.13727225363254547, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.578965663909912:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.5877058506011963:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.5966582298278809:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6057822704315186:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.614286184310913:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6235644817352295:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6329169273376465:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6414220333099365:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6500670909881592:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.659182071685791:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6682612895965576:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.676769495010376:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6857712268829346:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6947729587554932:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7037749290466309:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7127792835235596:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7217793464660645:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7307806015014648:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.739799976348877:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7488014698028564:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.13724173605442047, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7577235698699951:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.19998779892921448, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7667250633239746:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3097933828830719, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7757275104522705:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3568529188632965, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7847294807434082:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3646961748600006, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.793757677078247:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.803060531616211:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8114731311798096:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8204774856567383:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3882259726524353, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8294808864593506:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3882259726524353, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.838482141494751:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8474845886230469:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8564858436584473:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3882259726524353, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8654875755310059:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.874495506286621:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3725394308567047, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8836193084716797:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3646961748600006, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8928289413452148:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3568529188632965, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9014475345611572:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3490096628665924, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.91013503074646:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3333231508731842, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9191827774047852:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2862636148929596, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.928185224533081:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9366953372955322:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.16077150404453278, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9456963539123535:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.95493745803833:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.963944435119629:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9725258350372314:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9815285205841064:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9905309677124023:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.10589922964572906, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9995334148406982:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.10589922964572906, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.008535146713257:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.11374248564243317, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.017536163330078:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.11374248564243317, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.026538372039795:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.11374248564243317, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.03554105758667:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.11374248564243317, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.044577121734619:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.11374248564243317, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0535809993743896:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.12158574163913727, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0625839233398438:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.15295876562595367, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0715854167938232:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.16864527761936188, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.080662965774536:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.18433180451393127, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.089923620223999:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.20001831650733948, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0984323024749756:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.20786157250404358, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1074349880218506:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.22354808449745178, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1165573596954346:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.23139134049415588, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1249184608459473:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.22354808449745178, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.133427619934082:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2549211084842682, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.142526149749756:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2784508764743805, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1516470909118652:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.2941373884677887, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1607882976531982:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3098239004611969, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.169795036315918:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3255104124546051, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1787972450256348:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3333536684513092, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1878750324249268:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3333536684513092, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.19632887840271:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3333536684513092, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2053475379943848:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3490401804447174, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.214050769805908:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3647266924381256, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2230520248413086:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3804132342338562, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.231560468673706:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.240565299987793:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2495667934417725:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.258568525314331:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.267576217651367:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.276577949523926:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.285395622253418:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2938103675842285:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3960997462272644, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.3028154373168945:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=1.0, pitch=-0.3960997462272644, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.311816930770874:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=1.0, pitch=-0.3960997462272644, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3208184242248535:
            self.controls = SimpleControllerState(throttle=0.9647053480148315, steer=1.0, pitch=-0.3960997462272644, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.329820394515991:
            self.controls = SimpleControllerState(throttle=0.9019593000411987, steer=1.0, pitch=-0.3960997462272644, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.338822841644287:
            self.controls = SimpleControllerState(throttle=0.8862727880477905, steer=1.0, pitch=-0.3882564902305603, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3476788997650146:
            self.controls = SimpleControllerState(throttle=0.8862727880477905, steer=1.0, pitch=-0.3647266924381256, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3564531803131104:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.3490401804447174, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.365455150604248:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.3411969244480133, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.374192714691162:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.317667156457901, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3834168910980225:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.317667156457901, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.3928582668304443:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=1.0, pitch=-0.3255104124546051, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4013655185699463:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=1.0, pitch=-0.23923459649085999, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4103691577911377:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=0.9137241840362549, pitch=-0.20786157250404358, yaw=0.9137241840362549, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4193708896636963:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.7882320880889893, pitch=-0.19217506051063538, yaw=0.7882320880889893, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4286916255950928:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=0.6470534205436707, pitch=-0.16864527761936188, yaw=0.6470534205436707, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.43766713142395:
            self.controls = SimpleControllerState(throttle=0.8666646480560303, steer=0.4901883006095886, pitch=-0.14511550962924957, yaw=0.4901883006095886, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.446002721786499:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.3097933828830719, pitch=0.0, yaw=0.3097933828830719, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4550042152404785:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.464006185531616:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4724385738372803:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.481564521789551:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.489957809448242:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.498919725418091:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5075623989105225:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.516563653945923:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5255653858184814:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5348522663116455:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.543853998184204:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.552907943725586:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.17645801603794098, pitch=0.0, yaw=0.17645801603794098, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5619091987609863:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.3333231508731842, pitch=0.0, yaw=0.3333231508731842, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.570354700088501:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.599993884563446, pitch=-0.12158574163913727, yaw=0.599993884563446, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5793604850769043:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.7176427245140076, pitch=-0.16080202162265778, yaw=0.7176427245140076, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5880866050720215:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.7411724925041199, pitch=-0.18433180451393127, yaw=0.7411724925041199, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.596998453140259:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.749015748500824, pitch=-0.20001831650733948, yaw=0.749015748500824, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.605527877807617:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.7097994685173035, pitch=-0.20001831650733948, yaw=0.7097994685173035, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6143622398376465:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.5843073725700378, pitch=-0.20001831650733948, yaw=0.5843073725700378, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.623363971710205:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.5137180685997009, pitch=-0.20001831650733948, yaw=0.5137180685997009, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6323678493499756:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.4352855086326599, pitch=-0.17648853361606598, yaw=0.4352855086326599, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6414906978607178:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3646961748600006, pitch=-0.16864527761936188, yaw=0.3646961748600006, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6507368087768555:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3254798948764801, pitch=-0.16080202162265778, yaw=0.3254798948764801, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.659756660461426:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3254798948764801, pitch=-0.16080202162265778, yaw=0.3254798948764801, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6684107780456543:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3254798948764801, pitch=-0.16080202162265778, yaw=0.3254798948764801, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6769187450408936:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3411664068698883, pitch=-0.16864527761936188, yaw=0.3411664068698883, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.685426712036133:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.3803827166557312, pitch=-0.18433180451393127, yaw=0.3803827166557312, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6944286823272705:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.4588152766227722, pitch=-0.20001831650733948, yaw=0.4588152766227722, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7034311294555664:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.521561324596405, pitch=-0.23923459649085999, yaw=0.521561324596405, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7124321460723877:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=0.5686208605766296, pitch=-0.2706076204776764, yaw=0.5686208605766296, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.721458673477173:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.670583188533783, pitch=-0.2941373884677887, yaw=0.670583188533783, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7306876182556152:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.8196051120758057, pitch=-0.3019806444644928, yaw=0.8196051120758057, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.739258289337158:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.9529404640197754, pitch=-0.3019806444644928, yaw=0.9529404640197754, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7477481365203857:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=1.0, pitch=-0.3098239004611969, yaw=1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7567672729492188:
            self.controls = SimpleControllerState(throttle=0.8784295320510864, steer=1.0, pitch=-0.3098239004611969, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.765329599380493:
            self.controls = SimpleControllerState(throttle=0.921567440032959, steer=1.0, pitch=-0.3019806444644928, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.7746028900146484:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=1.0, pitch=-0.3019806444644928, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.783604860305786:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=1.0, pitch=-0.3019806444644928, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.7923543453216553:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3019806444644928, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.8007349967956543:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.317667156457901, yaw=1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.809521436691284:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9764702320098877, pitch=-0.3333536684513092, yaw=0.9764702320098877, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.818528413772583:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9137241840362549, pitch=-0.3882564902305603, yaw=0.9137241840362549, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.8278048038482666:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.843134880065918, pitch=-0.4980620741844177, yaw=0.843134880065918, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.8361704349517822:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.7097994685173035, pitch=-0.6157109141349792, yaw=0.7097994685173035, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.84492564201355:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.4745017886161804, pitch=-0.7804193496704102, yaw=0.4745017886161804, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.853929281234741:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 2.8629322052001953:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.87162184715271:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.52159184217453, pitch=-0.9843440055847168, yaw=0.0, roll=-0.52159184217453, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.8799567222595215:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6235541701316833, pitch=-0.9137547016143799, yaw=0.0, roll=-0.6235541701316833, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.8889505863189697:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=-0.6470839381217957, pitch=-0.8823816776275635, yaw=0.0, roll=-0.6470839381217957, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.897460460662842:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.6470839381217957, pitch=-0.8823816776275635, yaw=0.0, roll=-0.6470839381217957, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9064619541168213:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=-0.6392406821250916, pitch=-0.8823816776275635, yaw=0.0, roll=-0.6392406821250916, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.915741443634033:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=-0.6157109141349792, pitch=-0.8823816776275635, yaw=0.0, roll=-0.6157109141349792, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9242403507232666:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.5608081221580505, pitch=-0.9451277256011963, yaw=0.0, roll=-0.5608081221580505, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9333505630493164:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=-0.5059053301811218, pitch=-0.9686574935913086, yaw=0.0, roll=-0.5059053301811218, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9418447017669678:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4196295142173767, pitch=-0.9921872615814209, yaw=0.0, roll=-0.4196295142173767, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9508492946624756:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2941373884677887, pitch=-1.0, yaw=0.0, roll=-0.2941373884677887, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.959851026535034:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.18433180451393127, pitch=-1.0, yaw=0.0, roll=-0.18433180451393127, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.968852996826172:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.9778549671173096:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.22351756691932678, pitch=-1.0, yaw=0.0, roll=0.22351756691932678, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.986368179321289:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.4901883006095886, pitch=-1.0, yaw=0.0, roll=0.4901883006095886, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.994875431060791:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.6313669085502625, pitch=-0.9765007495880127, yaw=0.0, roll=0.6313669085502625, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.003256320953369:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.7176427245140076, pitch=-0.8823816776275635, yaw=0.0, roll=0.7176427245140076, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0116519927978516:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.7568590641021729, pitch=-0.843165397644043, yaw=0.0, roll=0.7568590641021729, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.02065372467041:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.764702320098877, pitch=-0.8353221416473389, yaw=0.0, roll=0.764702320098877, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.029655694961548:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.772545576095581, pitch=-0.8353221416473389, yaw=0.0, roll=0.772545576095581, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0388450622558594:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.7254859805107117, pitch=-0.8666951656341553, yaw=0.0, roll=0.7254859805107117, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.048002004623413:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.5450910925865173, pitch=-0.9843440055847168, yaw=0.0, roll=0.5450910925865173, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0570027828216553:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.3019501268863678, pitch=-1.0, yaw=0.0, roll=0.3019501268863678, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0658438205718994:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0742530822753906:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.082758665084839:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.15295876562595367, pitch=-1.0, yaw=0.0, roll=-0.15295876562595367, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0911641120910645:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.23139134049415588, pitch=-1.0, yaw=0.0, roll=-0.23139134049415588, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.100188970565796:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=-0.2706076204776764, pitch=-1.0, yaw=0.0, roll=-0.2706076204776764, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1091904640197754:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3098239004611969, pitch=-1.0, yaw=0.0, roll=-0.3098239004611969, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1184840202331543:
            self.controls = SimpleControllerState(throttle=0.9568620920181274, steer=-0.3411969244480133, pitch=-1.0, yaw=0.0, roll=-0.3411969244480133, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.127485990524292:
            self.controls = SimpleControllerState(throttle=0.8901944160461426, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1365466117858887:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.144914388656616:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.153918981552124:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1629209518432617:
            self.controls = SimpleControllerState(throttle=0.8274483680725098, steer=-0.3647266924381256, pitch=-1.0, yaw=0.0, roll=-0.3647266924381256, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1716747283935547:
            self.controls = SimpleControllerState(throttle=0.8156834840774536, steer=-0.3490401804447174, pitch=-1.0, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.180281639099121:
            self.controls = SimpleControllerState(throttle=0.8117618560791016, steer=-0.3098239004611969, pitch=-1.0, yaw=0.0, roll=-0.3098239004611969, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.189253807067871:
            self.controls = SimpleControllerState(throttle=0.8078402280807495, steer=-0.23139134049415588, pitch=-0.9765007495880127, yaw=0.0, roll=-0.23139134049415588, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1983776092529297:
            self.controls = SimpleControllerState(throttle=0.8039186000823975, steer=0.0, pitch=-0.8353221416473389, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.2073795795440674:
            self.controls = SimpleControllerState(throttle=0.7999969720840454, steer=0.0, pitch=-0.7176732420921326, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.216381549835205:
            self.controls = SimpleControllerState(throttle=0.7999969720840454, steer=0.0, pitch=-0.670613706111908, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.2247536182403564:
            self.controls = SimpleControllerState(throttle=0.7960753440856934, steer=0.0, pitch=-0.600024402141571, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.233755350112915:
            self.controls = SimpleControllerState(throttle=0.7882320880889893, steer=0.0, pitch=-0.5529648661613464, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.242757797241211:
            self.controls = SimpleControllerState(throttle=0.7607806921005249, steer=0.0, pitch=-0.4980620741844177, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.2511146068573:
            self.controls = SimpleControllerState(throttle=0.7450941205024719, steer=0.0, pitch=-0.4588457942008972, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.2601170539855957:
            self.controls = SimpleControllerState(throttle=0.7372508645057678, steer=0.0, pitch=-0.4274727702140808, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.269474506378174:
            self.controls = SimpleControllerState(throttle=0.7254859805107117, steer=0.0, pitch=-0.4117862582206726, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.2785556316375732:
            self.controls = SimpleControllerState(throttle=0.6784264445304871, steer=0.0, pitch=-0.3804132342338562, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.28755784034729:
            self.controls = SimpleControllerState(throttle=0.6588183045387268, steer=0.0, pitch=-0.3490401804447174, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.296560525894165:
            self.controls = SimpleControllerState(throttle=0.6352885365486145, steer=0.0, pitch=-0.3255104124546051, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3055617809295654:
            self.controls = SimpleControllerState(throttle=0.6039155125617981, steer=0.0, pitch=-0.2784508764743805, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3145532608032227:
            self.controls = SimpleControllerState(throttle=0.5725424885749817, steer=0.0, pitch=-0.19217506051063538, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3235552310943604:
            self.controls = SimpleControllerState(throttle=0.5450910925865173, steer=0.0, pitch=-0.13727225363254547, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3328707218170166:
            self.controls = SimpleControllerState(throttle=0.517639696598053, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.34131121635437:
            self.controls = SimpleControllerState(throttle=0.4980315566062927, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.349952459335327:
            self.controls = SimpleControllerState(throttle=0.4745017886161804, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.358935594558716:
            self.controls = SimpleControllerState(throttle=0.45489364862442017, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3679378032684326:
            self.controls = SimpleControllerState(throttle=0.443128764629364, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.376326560974121:
            self.controls = SimpleControllerState(throttle=0.4274422526359558, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3849551677703857:
            self.controls = SimpleControllerState(throttle=0.4039124846458435, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.3939590454101562:
            self.controls = SimpleControllerState(throttle=0.38430434465408325, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.4029617309570312:
            self.controls = SimpleControllerState(throttle=0.3568529188632965, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.411351203918457:
            self.controls = SimpleControllerState(throttle=0.34508803486824036, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.420356273651123:
            self.controls = SimpleControllerState(throttle=0.317636638879776, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.429358959197998:
            self.controls = SimpleControllerState(throttle=0.29802849888801575, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.4385147094726562:
            self.controls = SimpleControllerState(throttle=0.27449873089790344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.447519540786743:
            self.controls = SimpleControllerState(throttle=0.2548905909061432, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.4559314250946045:
            self.controls = SimpleControllerState(throttle=0.22351756691932678, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.464933156967163:
            self.controls = SimpleControllerState(throttle=0.20390942692756653, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.473353624343872:
            self.controls = SimpleControllerState(throttle=0.15684987604618073, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.48236083984375:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.4915618896484375:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5011632442474365:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5095643997192383:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.517928123474121:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.526930332183838:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.53576922416687:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.544152021408081:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5531976222991943:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5615572929382324:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5705623626708984:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5795650482177734:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5885658264160156:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5975701808929443:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.60657000541687:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.615572452545166:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6245744228363037:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6335761547088623:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6420793533325195:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6510837078094482:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6600866317749023:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6690874099731445:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.677593231201172:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6865952014923096:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6955981254577637:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7041070461273193:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7127885818481445:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.72145414352417:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.729987621307373:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7383878231048584:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7468132972717285:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7558138370513916:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7648167610168457:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7738654613494873:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7828688621520996:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7918691635131836:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.800870895385742:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.809382438659668:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8187649250030518:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8279175758361816:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8369197845458984:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.845921754837036:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8551056385040283:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8641088008880615:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.873110771179199:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.88161563873291:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8906197547912598:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8991267681121826:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9084231853485107:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.917428731918335:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.92684006690979:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9357094764709473:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9447121620178223:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9537129402160645:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9627158641815186:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.971717119216919:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9807190895080566:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.989253282546997:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9978044033050537:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0069990158081055:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.016556024551392:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.024911403656006:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0335469245910645:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.042751789093018:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0516510009765625:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.060295820236206:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0688254833221436:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.0779523849487305:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.086959362030029:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.096287250518799:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.105289697647095:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.114291191101074:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.123293161392212:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.13229513168335:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.141297340393066:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.150373220443726:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        else:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
            self.finished = self.timer > 4.159508943557739

        self.timer += dt
