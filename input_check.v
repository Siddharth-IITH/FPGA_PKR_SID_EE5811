module input_check(
	input clk,
	input [7:0] x_in,
	output [7:0] y_out
);

  reg [7:0] temp;

  initial begin
  reg temp1=1;
  end
  
  assign y_out = temp;

  always@(posedge clk) begin
	temp[0] <= temp1 - x_in[0];
	temp[1] <= temp1 - x_in[1];
	temp[2] <= temp1 - x_in[2];
	temp[3] <= temp1 - x_in[3];
	temp[4] <= temp1 - x_in[4];
	temp[5] <= temp1 - x_in[5];
	temp[6] <= temp1 - x_in[6];
	temp[7] <= temp1 - x_in[7];
  end

endmodule
	
