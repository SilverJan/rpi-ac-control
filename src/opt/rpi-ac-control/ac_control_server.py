from flask import Flask, request
from flask_restful import Resource, Api

from hvac_ircontrol.ir_sender import LogLevel
from hvac_ircontrol.mitsubishi import Mitsubishi, ClimateMode, FanMode, VanneVerticalMode, VanneHorizontalMode, ISeeMode, AreaMode, PowerfulMode

import utils

app = Flask(__name__)
api = Api(app)


class AcControl(Resource):
    def get(self, cmd):
        if cmd == "version":
            return "1.0.0", 200

        if cmd == "turnOff":
            ac.power_off()
            logger.info("turning AC off")
            return 200

        if cmd == "turnOn":
            logger.info("turning AC on")
            ac.send_command(
                climate_mode=ClimateMode.Cold,
                temperature=25,
                fan_mode=FanMode.Silent,
                vanne_vertical_mode=VanneVerticalMode.Top,
                vanne_horizontal_mode=VanneHorizontalMode.NotSet,
                isee_mode=ISeeMode.ISeeOn,
                area_mode=AreaMode.Full,
                powerful=PowerfulMode.PowerfulOff
            )
            return 200

        if cmd == "custom":
            temperature = 25
            fanMode = 'Silent'

            if 'temperature' in request.args.keys:
                temperature = int(request.args.get('temperature'))
                if temperature < 18 or temperature > 30:
                    return f"invalid temperature: {temperature}", 400
                logger.info(f"setting AC to {temperature} degrees")

            if 'fan' in request.args.keys:
                fanMode = request.args.get('fan')
                if fanMode not in ['Silent', 'Speed1', 'Speed2', 'Speed3']:
                    return f"invalid fan setting: {fanMode}", 400
                logger.info(f"setting AC to '{fanMode}' mode")

            ac.send_command(
                climate_mode=ClimateMode.Cold,
                temperature=temperature,
                fan_mode=getattr(FanMode, fanMode),
                vanne_vertical_mode=VanneVerticalMode.Top,
                vanne_horizontal_mode=VanneHorizontalMode.NotSet,
                isee_mode=ISeeMode.ISeeOn,
                area_mode=AreaMode.Full,
                powerful=PowerfulMode.PowerfulOff
            )
            return 200

        else:
            return "command not known", 404


api.add_resource(AcControl, '/<string:cmd>')

if __name__ == '__main__':
    logger = utils.get_logger('ac-control')
    ac = Mitsubishi(22, LogLevel.ErrorsOnly)
    app.run(host='0.0.0.0', port=5000, debug=True)
