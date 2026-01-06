import colorgram

# Extract 6 colors from an image
colors = colorgram.extract('D:\downloadrandom\Projects_Udemy_100DaysOfPython_byAngelaYu\Day_18-100\The Hirst Painting Project part 1 & 2\hirst_painting_dots.jpg', 6)

# Access the first color
first_color = colors[0]
rgb = first_color.rgb 

# Get the R, G, B components
r = rgb.r
g = rgb.g
b = rgb.b

# Print the RGB values
print(f"R: {r}, G: {g}, B: {b}")

# You can also iterate through all the colors
for color in colors:
    print(f"RGB: {color.rgb}, Proportion: {color.proportion:.2f}%")
