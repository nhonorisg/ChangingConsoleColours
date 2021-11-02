import random
import sty

# generateRGB() returns random RGB values using the randint() function
def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)

    return red, green, blue

# generateFGColours(<par1>,<par2>,<par3>) uses the function fg() to 
# change the text colour from generated RGB values
def generateFGColours(redCol, greenCol, blueCol):
    return sty.fg(redCol, greenCol, blueCol)

# generateBGColours(<par1>,<par2>,<par3>) uses the function bg() to
# change the backgroung colour from generated RGB values
def generateBGColours(redBG, greenBG, blueBG):
    return sty.bg(redBG, greenBG, blueBG)


redVal, greenVal, blueVal = generateRGB()  # generateRGB() have to be affected to a tripplet because it returns a tripplet
redBgVal, greenBgVal, blueBgVal = generateRGB()
colors = generateFGColours(redVal, greenVal, blueVal)
BgColors = generateBGColours(redBgVal, greenBgVal, blueBgVal)

print(BgColors, colors)  
# note that this first print have to above all those print statement in other to see colour changes
print(f"red = {redVal}, green = {greenVal}, blue = {blueVal}")
print(f"red backgroundColor = {redBgVal}, green backgroundColor = {greenBgVal}, blue backgroundColor = {blueBgVal}")
print("I am changing colours in my terminal :-)!!")
print(sty.ef.i, "this text will be italic")
print(sty.ef.b, "this text will be bold")
print(sty.ef.u, "this text will be underlined")