# fmt: off
from typing import Optional

from rlbot.agents.base_agent import SimpleControllerState


class CornerKickoff:
    def __init__(self):
        self.timer: float = 0.0
        self.finished: bool = False
        self.controls: Optional[SimpleControllerState] = None

    def step(self, dt: float):
        if self.timer == 0.0:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.009001731872558594:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.018012046813964844:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.02701544761657715:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.0355532169342041:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.044829368591308594:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.0532228946685791:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.06230020523071289:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.07119274139404297:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.07972097396850586:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.08885669708251953:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.09810042381286621:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.10710310935974121:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1164555549621582:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.12546014785766602:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.1344618797302246:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.14304018020629883:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.15215563774108887:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.16058063507080078:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.16990232467651367:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.17890381813049316:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.18790602684020996:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.19690799713134766:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2059335708618164:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2151041030883789:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2237253189086914:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.23268747329711914:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.24192023277282715:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.25121545791625977:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2597317695617676:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2690281867980957:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.27823805809020996:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.28670334815979004:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.2960352897644043:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3050413131713867:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3140430450439453:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3233315944671631:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3320937156677246:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.34136128425598145:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3504629135131836:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3594660758972168:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3684697151184082:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3774716854095459:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3867988586425781:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.3958008289337158:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.40438365936279297:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.41346073150634766:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4226498603820801:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.43171215057373047:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.44101667404174805:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4495096206665039:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4585130214691162:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4676799774169922:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.47680234909057617:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4861011505126953:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.4951033592224121:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5044307708740234:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5134320259094238:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5224344730377197:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5310993194580078:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5402257442474365:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5492279529571533:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5582294464111328:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5673220157623291:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5763182640075684:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5846595764160156:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.5937187671661377:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6024038791656494:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6113929748535156:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6203348636627197:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6293389797210693:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6378457546234131:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.646897554397583:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6560394763946533:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6644892692565918:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6737654209136963:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.682767391204834:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.6920900344848633:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7011144161224365:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7104225158691406:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7188055515289307:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7274231910705566:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7366127967834473:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.745185375213623:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7541873455047607:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7632112503051758:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7724101543426514:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7814607620239258:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7899622917175293:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.7989425659179688:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8075957298278809:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8168642520904541:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8259069919586182:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8348965644836426:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8439056873321533:
            self.controls = SimpleControllerState(throttle=0.14116336405277252, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8529102802276611:
            self.controls = SimpleControllerState(throttle=0.21567431092262268, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8619122505187988:
            self.controls = SimpleControllerState(throttle=0.26665547490119934, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.871068000793457:
            self.controls = SimpleControllerState(throttle=0.3097933828830719, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8803203105926514:
            self.controls = SimpleControllerState(throttle=0.37646105885505676, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8895134925842285:
            self.controls = SimpleControllerState(throttle=0.43136388063430786, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.8988394737243652:
            self.controls = SimpleControllerState(throttle=0.47842341661453247, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9073507785797119:
            self.controls = SimpleControllerState(throttle=0.5529343485832214, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9165158271789551:
            self.controls = SimpleControllerState(throttle=0.6588183045387268, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.92551589012146:
            self.controls = SimpleControllerState(throttle=0.7137210965156555, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9345171451568604:
            self.controls = SimpleControllerState(throttle=0.7568590641021729, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9437670707702637:
            self.controls = SimpleControllerState(throttle=0.7960753440856934, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9527702331542969:
            self.controls = SimpleControllerState(throttle=0.8274483680725098, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9612774848937988:
            self.controls = SimpleControllerState(throttle=0.8509781360626221, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9700143337249756:
            self.controls = SimpleControllerState(throttle=0.9294106960296631, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9788460731506348:
            self.controls = SimpleControllerState(throttle=0.9647053480148315, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 0.9878482818603516:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 0.9971299171447754:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.005704402923584:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.014815092086792:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.023817777633667:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.032407522201538:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0414111614227295:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.050678014755249:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.059173822402954:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0677306652069092:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0768566131591797:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.085418939590454:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.0944225788116455:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1029548645019531:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1113555431365967:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1205308437347412:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1290388107299805:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1374061107635498:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1457970142364502:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1542785167694092:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1627240180969238:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1717720031738281:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1807746887207031:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1893784999847412:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.1980197429656982:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.207021713256836:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2165021896362305:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2251040935516357:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2336249351501465:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2426259517669678:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2510347366333008:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.259542465209961:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2685441970825195:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2770516872406006:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.2854793071746826:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.29469633102417:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3030803203582764:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3122098445892334:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3214752674102783:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3298163414001465:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3388173580169678:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3478190898895264:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3563861846923828:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3651123046875:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.374361276626587:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.3832635879516602:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.14511550962924957, pitch=0.0, yaw=-0.14511550962924957, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.391780138015747:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2941373884677887, pitch=0.0, yaw=-0.2941373884677887, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4010977745056152:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5529648661613464, pitch=0.0, yaw=-0.5529648661613464, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4102630615234375:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.764732837677002, pitch=0.0, yaw=-0.764732837677002, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4192655086517334:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9765007495880127, pitch=0.0, yaw=-0.9765007495880127, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4277727603912354:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4361066818237305:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4451088905334473:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4541115760803223:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4625658988952637:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.471015453338623:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4800174236297607:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.488462209701538:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.4974689483642578:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.506230115890503:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5146639347076416:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.14511550962924957, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 1.5233120918273926:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.19217506051063538, yaw=-1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.5323450565338135:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.2549211084842682, yaw=-1.0, roll=0.0, jump=True, boost=True, handbrake=False)
        elif self.timer <= 1.541346549987793:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.317667156457901, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5504460334777832:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8980681896209717, pitch=-0.3568834364414215, yaw=0.0, roll=-0.8980681896209717, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.558905839920044:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7961058616638184, pitch=-0.3960997462272644, yaw=0.0, roll=-0.7961058616638184, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.567908763885498:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4902188181877136, pitch=-0.4274727702140808, yaw=0.0, roll=-0.4902188181877136, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5768325328826904:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.21570482850074768, pitch=-0.443159282207489, yaw=0.0, roll=-0.21570482850074768, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.586101770401001:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=-0.4510025382041931, yaw=0.0, roll=0.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.5945971012115479:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.3568529188632965, pitch=-0.4902188181877136, yaw=0.0, roll=0.3568529188632965, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6031005382537842:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.6392101645469666, pitch=-0.5059053301811218, yaw=0.0, roll=0.6392101645469666, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.612104892730713:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9764702320098877, pitch=-0.4980620741844177, yaw=0.0, roll=0.9764702320098877, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6212849617004395:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9843134880065918, pitch=-0.4745323061943054, yaw=0.0, roll=0.9843134880065918, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.630455493927002:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6397347450256348:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3882564902305603, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6483066082000732:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3255104124546051, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6573107242584229:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.3019806444644928, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6663129329681396:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.23139134049415588, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.6758003234863281:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.18433180451393127, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6844122409820557:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.15295876562595367, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.6934397220611572:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=-0.12942899763584137, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7024412155151367:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7113525867462158:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7204599380493164:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.7295124530792236:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 1.73785400390625:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7468175888061523:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.755396842956543:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7643990516662598:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7734005451202393:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.12939848005771637, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7818567752838135:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.14508499205112457, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.7910287380218506:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.16077150404453278, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8000304698944092:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.20783105492591858, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.809032917022705:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8180344104766846:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23920407891273499, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.827040672302246:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2548905909061432, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.836052417755127:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2784203588962555, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8450534343719482:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2941068708896637, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.854055643081665:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.863408088684082:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8718080520629883:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.880810260772705:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8898119926452637:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.8988144397735596:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9075071811676025:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9168181419372559:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9258050918579102:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2941068708896637, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9348087310791016:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9438481330871582:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3019501268863678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9528520107269287:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2941068708896637, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9618539810180664:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2705771028995514, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9710373878479004:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2548905909061432, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.980039358139038:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2470473349094391, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9890410900115967:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23920407891273499, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 1.9980435371398926:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23920407891273499, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.006556272506714:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23920407891273499, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.016038656234741:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23920407891273499, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0251400470733643:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0341460704803467:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0426526069641113:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0519280433654785:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.060434579849243:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.069438934326172:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0784413814544678:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0876359939575195:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.0961458683013916:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.105147361755371:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1136562824249268:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1226577758789062:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.131659984588623:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1406614780426025:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1496639251708984:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1583309173583984:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1669681072235107:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.175968885421753:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.1849706172943115:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.19397234916687:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.202974319458008:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2119765281677246:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.22351756691932678, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.220906972885132:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.23136082291603088, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.229980707168579:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2470473349094391, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2389824390411377:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.2784203588962555, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2479848861694336:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3097933828830719, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2569868564605713:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3254798948764801, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.26598858833313:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3411664068698883, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.2751057147979736:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3568529188632965, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.2841074466705322:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3568529188632965, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.29310941696167:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3646961748600006, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3016555309295654:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3803827166557312, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.310657501220703:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.3960692286491394, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.319831132888794:
            self.controls = SimpleControllerState(throttle=1.0, steer=1.0, pitch=0.4039124846458435, yaw=1.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3288321495056152:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9843134880065918, pitch=0.4274422526359558, yaw=0.9843134880065918, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3378348350524902:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9843134880065918, pitch=0.4509720206260681, yaw=0.9843134880065918, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3468236923217773:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9764702320098877, pitch=0.4588152766227722, yaw=0.9764702320098877, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3558273315429688:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.9372539520263672, pitch=0.4588152766227722, yaw=0.9372539520263672, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.364830493927002:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.8509781360626221, pitch=0.4666585326194763, yaw=0.8509781360626221, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3738319873809814:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.8039186000823975, pitch=0.4666585326194763, yaw=0.8039186000823975, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3829195499420166:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.749015748500824, pitch=0.4666585326194763, yaw=0.749015748500824, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.3919456005096436:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.6392101645469666, pitch=0.4509720206260681, yaw=0.6392101645469666, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.4009480476379395:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.5450910925865173, pitch=0.4039124846458435, yaw=0.5450910925865173, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.40994930267334:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.4588152766227722, pitch=0.3568529188632965, yaw=0.4588152766227722, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.4189512729644775:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.3568529188632965, pitch=0.317636638879776, yaw=0.3568529188632965, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.4281399250030518:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.19214454293251038, pitch=0.16861476004123688, yaw=0.19214454293251038, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.4365134239196777:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=False)
        elif self.timer <= 2.445514440536499:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.454517126083374:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.463550090789795:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.472064733505249:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.12942899763584137, pitch=0.0, yaw=-0.12942899763584137, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4810731410980225:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.21570482850074768, pitch=0.0, yaw=-0.21570482850074768, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.4902124404907227:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=-0.2627643644809723, pitch=0.0, yaw=-0.2627643644809723, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.499479293823242:
            self.controls = SimpleControllerState(throttle=0.9921567440032959, steer=-0.3019806444644928, pitch=0.0, yaw=-0.3019806444644928, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5079805850982666:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=-0.3333536684513092, pitch=0.0, yaw=-0.3333536684513092, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.516964912414551:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3333536684513092, pitch=0.0, yaw=-0.3333536684513092, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5260980129241943:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3411969244480133, pitch=0.0, yaw=-0.3411969244480133, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.535098075866699:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3411969244480133, pitch=0.0, yaw=-0.3411969244480133, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.544100284576416:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3411969244480133, pitch=0.0, yaw=-0.3411969244480133, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5524346828460693:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=-0.3333536684513092, pitch=0.0, yaw=-0.3333536684513092, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.5614256858825684:
            self.controls = SimpleControllerState(throttle=0.9803918600082397, steer=-0.3255104124546051, pitch=0.0, yaw=-0.3255104124546051, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.570220470428467:
            self.controls = SimpleControllerState(throttle=0.9764702320098877, steer=-0.317667156457901, pitch=0.0, yaw=-0.317667156457901, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.579226016998291:
            self.controls = SimpleControllerState(throttle=0.9607837200164795, steer=-0.3098239004611969, pitch=0.0, yaw=-0.3098239004611969, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.587712287902832:
            self.controls = SimpleControllerState(throttle=0.9333323240280151, steer=-0.3019806444644928, pitch=0.0, yaw=-0.3019806444644928, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.596229314804077:
            self.controls = SimpleControllerState(throttle=0.9137241840362549, steer=-0.2941373884677887, pitch=0.0, yaw=-0.2941373884677887, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.605231761932373:
            self.controls = SimpleControllerState(throttle=0.9019593000411987, steer=-0.2941373884677887, pitch=0.0, yaw=-0.2941373884677887, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6142334938049316:
            self.controls = SimpleControllerState(throttle=0.8941160440444946, steer=-0.317667156457901, pitch=0.0, yaw=-0.317667156457901, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6232352256774902:
            self.controls = SimpleControllerState(throttle=0.8862727880477905, steer=-0.3333536684513092, pitch=0.0, yaw=-0.3333536684513092, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.632431745529175:
            self.controls = SimpleControllerState(throttle=0.8823511600494385, steer=-0.4117862582206726, pitch=0.0, yaw=-0.4117862582206726, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6408469676971436:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=-0.4666890501976013, pitch=0.0, yaw=-0.4666890501976013, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.649458169937134:
            self.controls = SimpleControllerState(throttle=0.8705862760543823, steer=-0.5059053301811218, pitch=0.0, yaw=-0.5059053301811218, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6584341526031494:
            self.controls = SimpleControllerState(throttle=0.8666646480560303, steer=-0.5294350981712341, pitch=0.0, yaw=-0.5294350981712341, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6676039695739746:
            self.controls = SimpleControllerState(throttle=0.8548997640609741, steer=-0.5608081221580505, pitch=0.0, yaw=-0.5608081221580505, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.6764349937438965:
            self.controls = SimpleControllerState(throttle=0.843134880065918, steer=-0.6078676581382751, pitch=0.0, yaw=-0.6078676581382751, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.685028314590454:
            self.controls = SimpleControllerState(throttle=0.8392132520675659, steer=-0.6157109141349792, pitch=0.0, yaw=-0.6157109141349792, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.694030284881592:
            self.controls = SimpleControllerState(throttle=0.8352916240692139, steer=-0.6235541701316833, pitch=0.0, yaw=-0.6235541701316833, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7030327320098877:
            self.controls = SimpleControllerState(throttle=0.8313699960708618, steer=-0.6313974261283875, pitch=0.0, yaw=-0.6313974261283875, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7114369869232178:
            self.controls = SimpleControllerState(throttle=0.8274483680725098, steer=-0.6235541701316833, pitch=0.0, yaw=-0.6235541701316833, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7204837799072266:
            self.controls = SimpleControllerState(throttle=0.8235267400741577, steer=-0.6392406821250916, pitch=0.0, yaw=-0.6392406821250916, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7289934158325195:
            self.controls = SimpleControllerState(throttle=0.8117618560791016, steer=-0.6470839381217957, pitch=0.0, yaw=-0.6470839381217957, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7382025718688965:
            self.controls = SimpleControllerState(throttle=0.8078402280807495, steer=-0.6863002181053162, pitch=0.0, yaw=-0.6863002181053162, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.747204303741455:
            self.controls = SimpleControllerState(throttle=0.8039186000823975, steer=-0.7882626056671143, pitch=0.0, yaw=-0.7882626056671143, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.756206750869751:
            self.controls = SimpleControllerState(throttle=0.7921537160873413, steer=-0.9765007495880127, pitch=0.0, yaw=-0.9765007495880127, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.764714479446411:
            self.controls = SimpleControllerState(throttle=0.7882320880889893, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.7730751037597656:
            self.controls = SimpleControllerState(throttle=0.7803888320922852, steer=-1.0, pitch=0.0, yaw=-1.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 2.782198905944824:
            self.controls = SimpleControllerState(throttle=0.7803888320922852, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 2.7912003993988037:
            self.controls = SimpleControllerState(throttle=0.7843104600906372, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 2.8002023696899414:
            self.controls = SimpleControllerState(throttle=0.7999969720840454, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.808762788772583:
            self.controls = SimpleControllerState(throttle=0.8235267400741577, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.8178391456604004:
            self.controls = SimpleControllerState(throttle=0.8588213920593262, steer=-1.0, pitch=-0.10589922964572906, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.826840877532959:
            self.controls = SimpleControllerState(throttle=0.9607837200164795, steer=-1.0, pitch=-0.16864527761936188, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.836045503616333:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=-1.0, pitch=-0.20786157250404358, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.8450472354888916:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.2627643644809723, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.8540494441986084:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.2941373884677887, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.863332748413086:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.3255104124546051, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.8724424839019775:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.3255104124546051, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.881443977355957:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.3255104124546051, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.889953374862671:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.3255104124546051, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.898731231689453:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.3255104124546051, yaw=0.0, roll=-0.9921872615814209, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.9072461128234863:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.2941373884677887, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9163734912872314:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.23923459649085999, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.924964189529419:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.20786157250404358, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.933443069458008:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.19217506051063538, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9417831897735596:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=-0.15295876562595367, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.950989007949829:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9600629806518555:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.969064235687256:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 2.9780666828155518:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.9870684146881104:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 2.996098279953003:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0051002502441406:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0134544372558594:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0225744247436523:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0315778255462646:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.040724515914917:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.049382448196411:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.057889699935913:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.066502332687378:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.075504779815674:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0839920043945312:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.0929975509643555:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.1014468669891357:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=True, boost=True, handbrake=True)
        elif self.timer <= 3.1107757091522217:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.119868516921997:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.16861476004123688, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1284842491149902:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.22351756691932678, yaw=0.0, roll=-1.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1377201080322266:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9686574935913086, pitch=0.2862636148929596, yaw=0.0, roll=-0.9686574935913086, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.147033452987671:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9059114456176758, pitch=0.3568529188632965, yaw=0.0, roll=-0.9059114456176758, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.156092882156372:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8039491176605225, pitch=0.4588152766227722, yaw=0.0, roll=-0.8039491176605225, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1644346714019775:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6941434741020203, pitch=0.5137180685997009, yaw=0.0, roll=-0.6941434741020203, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.173464059829712:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5608081221580505, pitch=0.599993884563446, yaw=0.0, roll=-0.5608081221580505, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.181896924972534:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4510025382041931, pitch=0.6627399325370789, yaw=0.0, roll=-0.4510025382041931, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1908977031707764:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.3490401804447174, pitch=0.6862697005271912, yaw=0.0, roll=-0.3490401804447174, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.1999003887176514:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.23923459649085999, pitch=0.7333292365074158, yaw=0.0, roll=-0.23923459649085999, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2083725929260254:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.17648853361606598, pitch=0.7411724925041199, yaw=0.0, roll=-0.17648853361606598, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.21748423576355:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=0.749015748500824, yaw=0.0, roll=-0.12158574163913727, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2264862060546875:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.7568590641021729, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2355575561523438:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.764702320098877, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.244670867919922:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.772545576095581, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2535250186920166:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.772545576095581, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.262529134750366:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.772545576095581, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2715399265289307:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.10586871206760406, pitch=0.764702320098877, yaw=0.0, roll=0.10586871206760406, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.280545234680176:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.10586871206760406, pitch=0.764702320098877, yaw=0.0, roll=0.10586871206760406, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.2895472049713135:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.10586871206760406, pitch=0.772545576095581, yaw=0.0, roll=0.10586871206760406, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.298586130142212:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.764702320098877, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3076837062835693:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.7411724925041199, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.316779136657715:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.670583188533783, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.326050281524658:
            self.controls = SimpleControllerState(throttle=1.0, steer=0.0, pitch=0.6235236525535583, yaw=0.0, roll=0.0, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.334506034851074:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.10589922964572906, pitch=0.5921506285667419, yaw=0.0, roll=-0.10589922964572906, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.343404531478882:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=0.5686208605766296, yaw=0.0, roll=-0.12158574163913727, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3521728515625:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.20001831650733948, pitch=0.5607776045799255, yaw=0.0, roll=-0.20001831650733948, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.361175060272217:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.2627643644809723, pitch=0.5607776045799255, yaw=0.0, roll=-0.2627643644809723, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3704755306243896:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.3333536684513092, pitch=0.5607776045799255, yaw=0.0, roll=-0.3333536684513092, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3794796466827393:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.4274727702140808, pitch=0.5529343485832214, yaw=0.0, roll=-0.4274727702140808, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3884825706481934:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.5608081221580505, pitch=0.5450910925865173, yaw=0.0, roll=-0.5608081221580505, jump=False, boost=True, handbrake=True)
        elif self.timer <= 3.3969647884368896:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.6470839381217957, pitch=0.5607776045799255, yaw=0.0, roll=-0.6470839381217957, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.406022548675537:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7019867300987244, pitch=0.5607776045799255, yaw=0.0, roll=-0.7019867300987244, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4150238037109375:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.7804193496704102, pitch=0.521561324596405, yaw=0.0, roll=-0.7804193496704102, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4244441986083984:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8823816776275635, pitch=0.4274422526359558, yaw=0.0, roll=-0.8823816776275635, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4334523677825928:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9137547016143799, pitch=0.3490096628665924, yaw=0.0, roll=-0.9137547016143799, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.442765235900879:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9686574935913086, pitch=0.2705771028995514, yaw=0.0, roll=-0.9686574935913086, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.451531171798706:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.16861476004123688, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4605331420898438:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4696295261383057:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4781744480133057:
            self.controls = SimpleControllerState(throttle=1.0, steer=-1.0, pitch=0.0, yaw=0.0, roll=-1.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.4866793155670166:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.9372844696044922, pitch=0.0, yaw=0.0, roll=-0.9372844696044922, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.495896816253662:
            self.controls = SimpleControllerState(throttle=1.0, steer=-0.8196356296539307, pitch=0.0, yaw=0.0, roll=-0.8196356296539307, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5048987865448:
            self.controls = SimpleControllerState(throttle=0.996078372001648, steer=-0.6549271941184998, pitch=0.0, yaw=0.0, roll=-0.6549271941184998, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5139002799987793:
            self.controls = SimpleControllerState(throttle=0.9882351160049438, steer=-0.4196295142173767, pitch=0.0, yaw=0.0, roll=-0.4196295142173767, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5229029655456543:
            self.controls = SimpleControllerState(throttle=0.9843134880065918, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.531904697418213:
            self.controls = SimpleControllerState(throttle=0.9529404640197754, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5409088134765625:
            self.controls = SimpleControllerState(throttle=0.8941160440444946, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.549919605255127:
            self.controls = SimpleControllerState(throttle=0.8745079040527344, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.5585596561431885:
            self.controls = SimpleControllerState(throttle=0.8666646480560303, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=True)
        elif self.timer <= 3.567561626434326:
            self.controls = SimpleControllerState(throttle=0.8627430200576782, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.576563596725464:
            self.controls = SimpleControllerState(throttle=0.84705650806427, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.5855655670166016:
            self.controls = SimpleControllerState(throttle=0.8392132520675659, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.59456729888916:
            self.controls = SimpleControllerState(throttle=0.8313699960708618, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.603623151779175:
            self.controls = SimpleControllerState(throttle=0.8235267400741577, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.612886428833008:
            self.controls = SimpleControllerState(throttle=0.8078402280807495, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6219863891601562:
            self.controls = SimpleControllerState(throttle=0.7999969720840454, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.630988597869873:
            self.controls = SimpleControllerState(throttle=0.7882320880889893, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6399905681610107:
            self.controls = SimpleControllerState(throttle=0.7607806921005249, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6489927768707275:
            self.controls = SimpleControllerState(throttle=0.7372508645057678, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.657994508743286:
            self.controls = SimpleControllerState(throttle=0.7058778405189514, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.666996717453003:
            self.controls = SimpleControllerState(throttle=0.6901913285255432, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.6759984493255615:
            self.controls = SimpleControllerState(throttle=0.6784264445304871, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.685000419616699:
            self.controls = SimpleControllerState(throttle=0.6548966765403748, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.694002628326416:
            self.controls = SimpleControllerState(throttle=0.6431317925453186, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7025067806243896:
            self.controls = SimpleControllerState(throttle=0.6313669085502625, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7113749980926514:
            self.controls = SimpleControllerState(throttle=0.6117587685585022, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7203474044799805:
            self.controls = SimpleControllerState(throttle=0.5529343485832214, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7293403148651123:
            self.controls = SimpleControllerState(throttle=0.517639696598053, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.737755298614502:
            self.controls = SimpleControllerState(throttle=0.4941099286079407, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7469348907470703:
            self.controls = SimpleControllerState(throttle=0.45489364862442017, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.7559869289398193:
            self.controls = SimpleControllerState(throttle=0.4039124846458435, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.764920949935913:
            self.controls = SimpleControllerState(throttle=0.3568529188632965, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.773437023162842:
            self.controls = SimpleControllerState(throttle=0.30587175488471985, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.782421588897705:
            self.controls = SimpleControllerState(throttle=0.2470473349094391, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.791426420211792:
            self.controls = SimpleControllerState(throttle=0.20390942692756653, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8006293773651123:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8100924491882324:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.819096326828003:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.828098773956299:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8371005058288574:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8463587760925293:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8548812866210938:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.864452838897705:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8734893798828125:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.8826944828033447:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.891702175140381:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.900980234146118:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.910163402557373:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.918832302093506:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9278409481048584:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.936814546585083:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9452133178710938:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9537253379821777:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9622347354888916:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9711997509002686:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9804561138153076:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.989457845687866:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 3.9986367225646973:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.007906675338745:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.016608953475952:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.025002479553223:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        elif self.timer <= 4.033456563949585:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
        else:
            self.controls = SimpleControllerState(throttle=0.0, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False)
            self.finished = self.timer > 4.043089866638184

        self.timer += dt
