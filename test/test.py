import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge


@cocotb.test()
async def test_counter(dut):

    dut._log.info("START TEST")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # init
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # reset active
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # release reset
    dut.rst_n.value = 1

    # 🔥 IMPORTANT: wait for first real update
    await RisingEdge(dut.clk)

    # now counter should be 0 or 1 depending design
    value = int(dut.uo_out.value)

    dut._log.info(f"COUNTER={value}")

    # first valid step check
    await ClockCycles(dut.clk, 1)

    for i in range(1, 10):
        value = int(dut.uo_out.value)
        dut._log.info(f"COUNTER={value}")

        assert value == i, f"Expected {i}, Got {value}"

        await ClockCycles(dut.clk, 1)
