import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_counter(dut):

    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # RESET (ACTIVE LOW)
    dut.rst_n.value = 0
    dut.ena.value = 0
    dut.ui_in.value = 0

    await RisingEdge(dut.clk)

    dut.rst_n.value = 1  # release reset

    # load data
    dut.ena.value = 1
    dut.ui_in.value = 0xA5

    await RisingEdge(dut.clk)

    dut.ena.value = 0

    # shift test
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    assert dut.uo_out.value != 0
