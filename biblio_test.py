from numpy import *
import bibliopixel.drivers.serial_driver as driver
import bibliopixel.animation as animation
import bibliopixel.led as led

s = driver.DriverSerial(driver.LEDTYPE.APA102, 64*9, dev="/dev/ttyACM0")
led = led.LEDStrip(s)
led.setMasterBrightness(4)
print 'here'
# here

a = animation.StripChannelTest(led)
rgb = zeros((s.numLEDs, 3), uint8)
# s.update(rgb)
led.fill((255, 0, 0))
print dir(led)
# led.update()
for i in range(100):
    a.step()
# a.run()

