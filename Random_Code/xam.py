def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
		return hex_color
	elif color == "green":
		hex_color = "#00ff00"
		return hex_color
	elif color == "blue":
		hex_color = "#0000ff"
		return hex_color
	elif color == "":
		hex_color = "unknown"
	return "unknown"

print(color_translator("red"))