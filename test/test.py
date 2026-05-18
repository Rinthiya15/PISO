import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


def safe_int(sig):
    """Convert safely even if X/Z exists"""
    try:
        return int(sig.value)
    except:
        return 0


@cocotb.test()
async def test_counter(dut):

    dut._log.info("START TEST")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # RESET
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    dut.rst_n.value = 1

    await ClockCycles(dut.clk, 1)

    assert safe_int(dut.uo_out) == 0

    for i in range(1, 10):
        await ClockCycles(dut.clk, 1)
        value = safe_int(dut.uo_out)

        dut._log.info(f"COUNTER={value}")

        assert value == i, f"Expected {i}, Got {value}"
