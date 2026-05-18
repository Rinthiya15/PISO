`default_nettype none
`timescale 1ns / 1ps

module tb ();

  // Dump waveform
  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
  end

  // Inputs
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  // Outputs
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

  // DUT Instantiation
  tt_um_PISO dut (
      .ui_in(ui_in),
      .uo_out(uo_out),
      .uio_in(uio_in),
      .uio_out(uio_out),
      .uio_oe(uio_oe),
      .ena(ena),
      .clk(clk),
      .rst_n(rst_n)
  );

  // Clock Generation
  initial begin
    clk = 0;
    forever #5 clk = ~clk; // 10ns clock period
  end

  // Test Sequence
  initial begin

    // Initialize
    ena    = 1;
    rst_n  = 0;
    ui_in  = 8'h00;
    uio_in = 8'h00;

    // Hold reset
    #20;
    rst_n = 1;

    // Run simulation
    #200;

    $finish;
  end

  // Monitor outputs
  initial begin
    $monitor("TIME=%0t | RESET=%b | COUNTER=%h",
              $time, rst_n, uo_out);
  end

endmodule
