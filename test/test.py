# SPDX-FileCopyrightText: © 2024
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_counter(dut):

    dut._log.info("Starting Counter Test")

    # Create 10us clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Initialize signals
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Apply Reset
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)

    # Release Reset
    dut.rst_n.value = 1

    dut._log.info("Reset Released")

    # Check counter starts from 0
    assert dut.uo_out.value == 0, \
        f"Counter not reset properly! Got {int(dut.uo_out.value)}"

    # Check counter increments
    for i in range(1, 11):

        await ClockCycles(dut.clk, 1)

        counter_value = int(dut.uo_out.value)

        dut._log.info(
            f"Cycle={i} Counter={counter_value}"
        )

        assert counter_value == i, \
            f"Counter mismatch! Expected={i}, Got={counter_value}"

    dut._log.info("Counter Test Passed ✅")
