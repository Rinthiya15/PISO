module tt_um_PISO (
    input  wire clk,
    input  wire reset,      // ACTIVE HIGH reset (FIXED)
    input  wire ena,

    input  wire [7:0] ui_in,
    output reg  [7:0] uo_out,

    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe
);

    reg [7:0] shift_reg;

    always @(posedge clk) begin
        if (reset)
            shift_reg <= 8'b0;
        else if (ena)
            shift_reg <= ui_in;   // parallel load
        else
            shift_reg <= {shift_reg[6:0], 1'b0}; // shift
    end

    always @(*) begin
        uo_out = shift_reg;
    end

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
