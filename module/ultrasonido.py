from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class US(Module, AutoCSR):
    def __init__(self, echo, trig):
        self.clk = ClockSignal()
        self.echo = echo
        self.trig = trig
        self.dist = CSRStatus(9)

        self.specials += Instance("ultrasonido",
            i_clk = self.clk,
            i_echo = self.echo,
            o_trig = self.trig,
            o_dist = self.dist.status
          )
