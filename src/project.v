module tt_um_PISO (
    input  wire clk,
    input  wire rst_n,
    input  wire ena,
    input  wire ui_in,
    output wire uo_out
);

    // 8-bit shift register
    reg [7:0] shift_reg;

    always @(posedge clk) begin
        if (!rst_n)
            shift_reg <= 8'b0;
        else if (ena)
            shift_reg <= {shift_reg[6:0], ui_in};
    end

    assign uo_out = shift_reg[7];

endmodule
