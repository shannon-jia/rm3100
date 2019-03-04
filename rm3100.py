# -*- coding: utf-8 -*-

"""Main module."""

import logging
from spi_dev import Spi_Dev

log = logging.getLogger(__name__)


class QRM3100(object):

    QRM3100_CMM = 0x01
    QRM3100_CCXMSB = 0x04
    QRM3100_CCXLSB = 0x05
    QRM3100_CCYMSB = 0x06
    QRM3100_CCYLSB = 0x07
    QRM3100_CCZMSB = 0x08
    QRM3100_CCZLSB = 0x09
    QRM3100_NOS_REG = 0x0A
    QRM3100_TMRC = 0x0B
    QRM3100_MX2 = 0xA4
    QRM3100_MX1 = 0xA5
    QRM3100_MX0 = 0xA6
    QRM3100_MY2 = 0xA7
    QRM3100_MY1 = 0xA8
    QRM3100_MY0 = 0xA9
    QRM3100_MZ2 = 0xAA
    QRM3100_MZ1 = 0xAB
    QRM3100_MZ0 = 0xAC
    QRM3100_STATUS_REG = 0xB4
    QRM3100_I2C_ADDRESS = 0x20
    QRM3100_POLL = 0x00

    CALIBRATION_TIMEOUT = 5000
    DEG_PER_RAD = 180.0/3.14159265358979

    def __init__(self, spi=None):
        self.spi = spi

    def measure(self, address):
        res = self.spi.readRegister(address)
        return res

if __name__ == "__main__":
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                  "[%(module)s:%(lineno)d] %(message)s")
    # log the things
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(formatter)
    log.addHandler(ch)

    port = 0
    device = 0
    spi = Spi_Dev(port, device)
    rm3100 = QRM3100(spi)
    print(rm3100.measure(0x05))
    print(rm3100.measure(0x06))
    print(rm3100.measure(0x07))
    print(rm3100.measure(0x08))
    print(rm3100.measure(0x09))
    print(rm3100.measure(0x0A))
    print(rm3100.measure(0x0B))
    print(rm3100.measure(0xA4))
    print(rm3100.measure(0xA5))
    print(rm3100.measure(0xA6))
    print(rm3100.measure(0xA7))
    print(rm3100.measure(0xA8))
    print(rm3100.measure(0xA9))
    print(rm3100.measure(0xAA))
    print(rm3100.measure(0xAB))
    print(rm3100.measure(0xAC))
    print(rm3100.measure(0xB4))
    print(rm3100.measure(0x20))
    print(rm3100.measure(0x00))
