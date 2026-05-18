<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project is an 8-bit counter.  
The counter increments by 1 on every clock cycle and outputs the value on `uo_out[7:0]`.

---

## How to test

1. Apply clock to `clk`
2. Set `ena = 1`
3. Reset using `rst_n = 0`
4. Set `rst_n = 1`
5. Observe counter output on `uo_out`

---

## External hardware

Optional LEDs for viewing the counter output.
