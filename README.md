# lcd-i2c

A Python module to handle the I2C communication between a Raspberry Pi and an
i2c backpack for a 16x2 (or other size) char LCD.
This module supports screens with up to 4 lines. There's no maximum width.

You can simply import the lcd_i2c as shown in the example and easily print to the
display.


# Installation

To install this module, run the following commands:

```
    python setup.py build
    python setup.py install
```

The second command might need to run as superuser or using sudo.

# Usage

After creating a lcd_i2c object, you can use the following methods to write to the LCD:

```python
    println(string, line)               # Print only on one line. All characters which won't fit are ignored
    print(string, scroll_time = 5)      # Print a string. If the string is too big for the 
                                        #  lcd it will scroll through all the text.
    clear()                             # Remove all text from the screen
```

# License

The code in this project is licensed under the GNU GPL v3, or (at your option) any later version.
