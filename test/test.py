import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_counter(dut):

    dut._log.info("START TEST")

    # Inputs init FIRST (important)
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # settle time
    await Timer(1, "ns")

    # reset hold
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1

    # wait 1 cycle after reset
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == 0

    # check counter
    for i in range(1, 10):
        await ClockCycles(dut.clk, 1)
        value = int(dut.uo_out.value)

        dut._log.info(f"COUNT={value}")

        assert value == i, f"Expected {i}, Got {value}"

    dut._log.info("PASS ✅")
