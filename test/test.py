import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_counter(dut):

    # Clock start
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # RESET
    dut.reset.value = 0
    await Timer(20, units="ns")

    dut.reset.value = 1
    await RisingEdge(dut.clk)

    # check sequence
    expected = 0

    for i in range(5):
        await RisingEdge(dut.clk)

        value = dut.uo_out.value.integer   # IMPORTANT FIX 🔥

        dut._log.info(f"COUNTER={value}")

        assert value == expected, f"Expected {expected}, Got {value}"

        expected += 1
