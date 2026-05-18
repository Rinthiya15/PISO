module tt_um_PISO (
    input  wire [7:0] ui_in,     // input pins
    output wire [7:0] uo_out,    // output pins
    input  wire [7:0] uio_in,    // bidir input
    output wire [7:0] uio_out,   // bidir output
    output wire [7:0] uio_oe,    // output enable
    input  wire clk,
    input  wire rst_n
);

reg [7:0] counter;

always @(posedge clk) begin
    if (!rst_n)
        counter <= 0;
    else
        counter <= counter + 1;
end

assign uo_out = counter;

endmodule
