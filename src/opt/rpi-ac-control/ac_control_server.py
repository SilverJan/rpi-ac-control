from flask import Flask
from flask_restful import Resource, Api

from hvac_ircontrol.ir_sender import LogLevel
from hvac_ircontrol.mitsubishi import Mitsubishi, ClimateMode, FanMode, VanneVerticalMode, VanneHorizontalMode, ISeeMode, AreaMode, PowerfulMode

app = Flask(__name__)
api = Api(app)


class AcControl(Resource):
    def get(self, cmd):
        if cmd == "turnOff":
            ac.power_off()
            return 200
        if cmd == "turnOn":
            ac.send_command(
                climate_mode=ClimateMode.Cold,
                temperature=25,
                fan_mode=FanMode.Speed1,
                vanne_vertical_mode=VanneVerticalMode.Top,
                vanne_horizontal_mode=VanneHorizontalMode.NotSet,
                isee_mode=ISeeMode.ISeeOn,
                area_mode=AreaMode.Full,
                powerful=PowerfulMode.PowerfulOff
            )
            return 200

api.add_resource(AcControl, '/<string:cmd>')

if __name__ == '__main__':
    ac = Mitsubishi(22, LogLevel.ErrorsOnly)
    app.run(host='0.0.0.0', port=5000, debug=True)
