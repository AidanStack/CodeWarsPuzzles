#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
#representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
#be rounded to the closest valid value.

#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.



def rgb(r, g, b):
    hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
           13: 'D', 14: 'E', 15: 'F'}

    def hex_conv(x):
        if x < 0:
            x = 0
        if x > 255:
            x = 255
        hex1 = x // 16
        hex2 = (x / 16 - hex1) * 16
        return hex[hex1] + hex[hex2]

    return hex_conv(r) + hex_conv(g) + hex_conv(b)