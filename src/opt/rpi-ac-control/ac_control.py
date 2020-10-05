#!/usr/bin/env python3

import argparse
import utils
import logging
import sys

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
                        help='turn on AC with default values')
    parser.add_argument('--temp', dest='temperature', default=25, type=int,
                        help='define temperature')
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
    HVAC = Mitsubishi(22, LogLevel.ErrorsOnly)

    if args.turnOff:
        HVAC.power_off()

    if args.turnOn:
        HVAC.send_command(
            climate_mode=ClimateMode.Cold,
            temperature=25,
            fan_mode=FanMode.Speed1,
            vanne_vertical_mode=VanneVerticalMode.Top,
            vanne_horizontal_mode=VanneHorizontalMode.NotSet,
            isee_mode=ISeeMode.ISeeOn,
            area_mode=AreaMode.Full,
            powerful=PowerfulMode.PowerfulOff
        )
        sys.exit()

    if args.temperature:
        HVAC.send_command(
            climate_mode=ClimateMode.Cold,
            temperature=args.temperature,
            fan_mode=FanMode.Speed1,
            vanne_vertical_mode=VanneVerticalMode.Top,
            vanne_horizontal_mode=VanneHorizontalMode.NotSet,
            isee_mode=ISeeMode.ISeeOn,
            area_mode=AreaMode.Full,
            powerful=PowerfulMode.PowerfulOff
        )
        sys.exit()
