# -*- coding: utf-8 -*-


MSBFIRST = 0
LSBFIRST = 1


class Spi_Dev(object):
    """Hardware-based SPI implementation using the spidev interface."""

    def __init__(self, port, device, max_speed_hz=500000):
        """Initialize an SPI device using the SPIdev interface.  Port and device
        identify the device, for example the device /dev/spidev1.0 would be port
        1 and device 0.
        """
        import spidev
        self._device = spidev.SpiDev()
        self._device.open(port, device)
        self._device.max_speed_hz=max_speed_hz
        # Default to mode 0.
        self._device.mode = 0

    def set_clock_hz(self, hz):
        """Set the speed of the SPI clock in hertz.  Note that not all speeds
        are supported and a lower speed might be chosen by the hardware.
        """
        self._device.max_speed_hz=hz

    def set_mode(self, mode):
        """Set SPI mode which controls clock polarity and phase.  Should be a
        numeric value 0, 1, 2, or 3.  See wikipedia page for details on meaning:
        http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus
        """
        if mode < 0 or mode > 3:
            raise ValueError('Mode must be a value 0, 1, 2, or 3.')
        self._device.mode = mode

    def set_bit_order(self, order):
        """Set order of bits to be read/written over serial lines.  Should be
        either MSBFIRST for most-significant first, or LSBFIRST for
        least-signifcant first.
        """
        if order == MSBFIRST:
            self._device.lsbfirst = False
        elif order == LSBFIRST:
            self._device.lsbfirst = True
        else:
            raise ValueError('Order must be MSBFIRST or LSBFIRST.')

    def close(self):
        """Close communication with the SPI device."""
        self._device.close()

    def write(self, data):
        """Half-duplex SPI write.  The specified array of bytes will be clocked
        out the MOSI line.
        """
        self._device.writebytes(data)

    def read(self, length):
        """Half-duplex SPI read.  The specified length of bytes will be clocked
        in the MISO line and returned as a bytearray object.
        """
        return bytearray(self._device.readbytes(length))

    def transfer(self, data):
        """Full-duplex SPI read and write.  The specified array of bytes will be
        clocked out the MOSI line, while simultaneously bytes will be read from
        the MISO line.  Read bytes will be returned as a bytearray object.
        """
        return bytearray(self._device.xfer2(data))

    def readRegister(self, regAddr):
        """Read the value of the specified register."""
        address = 0x80 | regAddr
        resp = self._device.xfer2([address, 0x00]) 
        return resp[1]

    def writeRegister(self, regAddr, value):
        """Write a value to a specified register."""
        self._device.xfer2([regAddr, value])
