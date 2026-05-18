module counter (
    input wire clk,
    input wire reset,
    output reg [7:0] uo_out
);

always @(posedge clk) begin
    if (!reset)
        uo_out <= 8'd0;
    else
        uo_out <= uo_out + 1;
end

endmodule
