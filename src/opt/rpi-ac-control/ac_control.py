#!/usr/bin/env python3

import argparse
import utils
import logging

from hvac_ircontrol.ir_sender import LogLevel
from hvac_ircontrol.mitsubishi import Mitsubishi, ClimateMode, FanMode, VanneVerticalMode, VanneHorizontalMode, ISeeMode, AreaMode, PowerfulMode

logger = utils.get_logger("ac-control")

def handleArguments() -> None:
    """Handles CLI arguments and saves them globally"""
    parser = argparse.ArgumentParser(
        description="Allows controlling of AC."
    )
    parser.add_argument('--turn-off', dest='turnOff', default=False, action='store_true',
                        help='turn off AC')
    parser.add_argument('--turn-on', dest='turnOn', default=False, action='store_true',
                        help='turn off AC')
    parser.add_argument('--debug',
                        dest='debug', default=False, action='store_true',
                        help='turn debug mode on (default: False)')

    global args
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Running in DEBUG logging mode")

    logger.debug("Running with the following arguments: {}".format(args))

if __name__ == '__main__':
    handleArguments()

    # instantiate AC object
    HVAC = Mitsubishi(23, LogLevel.ErrorsOnly)

    HVAC.send_command(
        climate_mode=ClimateMode.Cold,
        temperature=18,
        fan_mode=FanMode.Auto,
        vanne_vertical_mode=VanneVerticalMode.Auto,
        vanne_horizontal_mode=VanneHorizontalMode.NotSet,
        isee_mode=ISeeMode.ISeeOn,
        area_mode=AreaMode.Full,
        powerful=PowerfulMode.PowerfulOn
    )
