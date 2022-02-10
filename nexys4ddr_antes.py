from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("led",  0, Pins("T8"), IOStandard("LVCMOS33")),
    ("led",  1, Pins("V9"), IOStandard("LVCMOS33")),
    ("led",  2, Pins("R8"), IOStandard("LVCMOS33")),
    ("led",  3, Pins("T6"), IOStandard("LVCMOS33")),
    ("led",  4, Pins("T5"), IOStandard("LVCMOS33")),
    ("led",  5, Pins("T4"), IOStandard("LVCMOS33")),
    ("led",  6, Pins("U7"), IOStandard("LVCMOS33")),
    ("led",  7, Pins("U6"), IOStandard("LVCMOS33")),
    ("led",  8, Pins("V4"), IOStandard("LVCMOS33")),
    ("led",  9, Pins("U3"), IOStandard("LVCMOS33")),
    ("led", 10, Pins("V1"), IOStandard("LVCMOS33")),
    ("led", 11, Pins("R1"), IOStandard("LVCMOS33")),

    ("sw",  0, Pins("U9"), IOStandard("LVCMOS33")),
    ("sw",  1, Pins("U8"), IOStandard("LVCMOS33")),
    ("sw",  2, Pins("R7"), IOStandard("LVCMOS33")),
    ("sw",  3, Pins("R6"), IOStandard("LVCMOS33")),
    ("sw",  4, Pins("R5"), IOStandard("LVCMOS33")),
    ("sw",  5, Pins("V7"), IOStandard("LVCMOS33")),
    ("sw",  6, Pins("V6"), IOStandard("LVCMOS33")),
    ("sw",  7, Pins("V5"), IOStandard("LVCMOS33")),
    
    ("btnc", 0, Pins("E16"), IOStandard("LVCMOS33")),
    ("btnr", 0, Pins("R10"), IOStandard("LVCMOS33")),
    ("btnl", 0, Pins("T16"), IOStandard("LVCMOS33")),

    ("ledRGB", 1,
        Subsignal("r", Pins("K5")),
        Subsignal("g", Pins("F13")),
        Subsignal("b", Pins("F6")),
        IOStandard("LVCMOS33")),

    ("ledRGB", 2,
        Subsignal("r", Pins("K6")),
        Subsignal("g", Pins("H6")),
        Subsignal("b", Pins("L16")),
        IOStandard("LVCMOS33")),
       
    ("display_digit",  0, Pins("N6"), IOStandard("LVCMOS33")),
    ("display_digit",  1, Pins("M6"), IOStandard("LVCMOS33")),
    ("display_digit",  2, Pins("M3"), IOStandard("LVCMOS33")),
    ("display_digit",  3, Pins("N5"), IOStandard("LVCMOS33")),
    ("display_digit",  4, Pins("N2"), IOStandard("LVCMOS33")),
    ("display_digit",  5, Pins("N4"), IOStandard("LVCMOS33")),
    ("display_digit",  6, Pins("L1"), IOStandard("LVCMOS33")),
    ("display_digit",  7, Pins("M1"), IOStandard("LVCMOS33")),
    ("display_segment", 0, Pins("L3"), IOStandard("LVCMOS33")),
    ("display_segment", 1, Pins("N1"), IOStandard("LVCMOS33")),
    ("display_segment", 2, Pins("L5"), IOStandard("LVCMOS33")),
    ("display_segment", 3, Pins("L4"), IOStandard("LVCMOS33")),
    ("display_segment", 4, Pins("K3"), IOStandard("LVCMOS33")),
    ("display_segment", 5, Pins("M2"), IOStandard("LVCMOS33")),
    ("display_segment", 6, Pins("L6"), IOStandard("LVCMOS33")),
    ("display_segment", 7, Pins("M4"), IOStandard("LVCMOS33")),
    
  	
    ("vga_red", 0, Pins("A3"), IOStandard("LVCMOS33")),
    ("vga_red", 1, Pins("B4"), IOStandard("LVCMOS33")),
    ("vga_red", 2, Pins("C5"), IOStandard("LVCMOS33")),
    ("vga_red", 3, Pins("A4"), IOStandard("LVCMOS33")),
    ("vga_green", 0, Pins("C6"), IOStandard("LVCMOS33")),
    ("vga_green", 1, Pins("A5"), IOStandard("LVCMOS33")),
    ("vga_green", 2, Pins("B6"), IOStandard("LVCMOS33")),
    ("vga_green", 3, Pins("A6"), IOStandard("LVCMOS33")),
    ("vga_blue", 0, Pins("B7"), IOStandard("LVCMOS33")),
    ("vga_blue", 1, Pins("C7"), IOStandard("LVCMOS33")),
    ("vga_blue", 2, Pins("D7"), IOStandard("LVCMOS33")),
    ("vga_blue", 3, Pins("D8"), IOStandard("LVCMOS33")),
    ("hsync", 0, Pins("B11"), IOStandard("LVCMOS33")),
    ("vsync", 0, Pins("B12"), IOStandard("LVCMOS33")),
    

    ("btnu", 0, Pins("F15"), IOStandard("LVCMOS33")),
 
    ("cam_xclk", 0, Pins("P2"), IOStandard("LVCMOS33")),
    ("cam_pclk", 0, Pins("V10"), IOStandard("LVCMOS33")),
 
    ("cam_data_in",  0, Pins("U4"), IOStandard("LVCMOS33")),
    ("cam_data_in",  1, Pins("V2"), IOStandard("LVCMOS33")),
    ("cam_data_in", 2, Pins("U2"), IOStandard("LVCMOS33")),
    ("cam_data_in", 3, Pins("T3"), IOStandard("LVCMOS33")),
    ("cam_data_in", 4, Pins("T1"), IOStandard("LVCMOS33")),
    ("cam_data_in", 5, Pins("R3"), IOStandard("LVCMOS33")),
    ("cam_data_in", 6, Pins("P3"), IOStandard("LVCMOS33")),
    ("cam_data_in", 7, Pins("P4"), IOStandard("LVCMOS33")),


    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),
    ("clk", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "J18 H17 H15 J17 H16 K15 K13 N15",
            "V16 U14 V14 V12 P14"),
            IOStandard("SSTL18_II")),
        Subsignal("ba", Pins("U16 R15 N14"), IOStandard("SSTL18_II")),
        Subsignal("ras_n", Pins("H14"), IOStandard("SSTL18_II")),
        Subsignal("cas_n", Pins("L18"), IOStandard("SSTL18_II")),
        Subsignal("we_n", Pins("R11"), IOStandard("SSTL18_II")),
        Subsignal("dm", Pins("J15 J13"), IOStandard("SSTL18_II")),
        Subsignal("dq", Pins(
            "R12 T11 U12 R13 U18 R17 T18 R18",
            "F18 G18 G17 M18 M17 P18 N17 P17"),
            IOStandard("SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_50")),
#LOS PINES SON DIFERENTES EN DDR. EN CRAM NO SE ENCUENTRA BA, CAS, RAS, DQS_P, DQS_N, CLK_P(CLK), CLK_N(WAIT), CKE(ADVN), CS
        Subsignal("dqs_p", Pins("U17 T10"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("M16 U13"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_p", Pins("T15"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("T14"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke", Pins("T13"), IOStandard("SSTL18_II")),
        Subsignal("odt", Pins("J14"), IOStandard("SSTL18_II")),
        Subsignal("cs_n", Pins("R15"), IOStandard("SSTL18_II")),
        Misc("SLEW=FAST"),
    ),

    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D5")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n", Pins("B3")),
        Subsignal("rx_data", Pins("C11 D10")),
        Subsignal("crs_dv", Pins("D9")),
        Subsignal("tx_en", Pins("B9")),
        Subsignal("tx_data", Pins("A10 A8")),
        Subsignal("mdc", Pins("C9")),
        Subsignal("mdio", Pins("A9")),
        Subsignal("rx_er", Pins("C10")),
        Subsignal("int_n", Pins("B8")),
        IOStandard("LVCMOS33")
     ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk"
    default_clk_period = 1e9/100e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-CSG324-1", _io, toolchain="vivado")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
