import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_counter(dut):

    dut._log.info("Starting Counter Test")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Init
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # RESET
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # Release reset
    dut.rst_n.value = 1

    # IMPORTANT: wait 1 cycle BEFORE checking
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == 0

    # Now check counting starts
    for i in range(1, 11):

        await ClockCycles(dut.clk, 1)
        value = int(dut.uo_out.value)

        dut._log.info(f"Counter = {value}")

        assert value == i, f"Expected {i}, Got {value}"

    dut._log.info("PASS ✅")
