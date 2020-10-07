# rpi-ac-control

Contains source code to build the `rpi-ac-control` Debian package, which installs an AC control tool
on the Raspberry Pi.

## Prerequisites

In order to function, it is expected that you have 

* A) configured a IR emitter on your Raspberry Pi

### A) IR emitter setup

The IR emitter should be connected to the Raspberry Pi like that:

<img src="res/dht11_raspberrypi_setup.jpg" alt="dht11_raspberrypi_setup.jpg" width="500"/>

Source: TBD

## How to install & setup the package

Install directly on your Raspberry Pi via

    make install

or

	./create_deb.sh
	sudo gdebi dist/rpi-ac-control_1.0.0_all.deb

## How to use the AC control

Once the service is started, you can control your AC by calling the following endpoints:

	http://<ip-address>:5000/turnOn # or turnon
	http://<ip-address>:5000/turnOff # or turnoff
	http://<ip-address>:5000/custom?temperature=25&fan=Silent

Example via curl:

	curl -f http://<ip-address>:5000/turnOn

## How to monitor / debug service

To verify the functionality of the service, check

	sudo systemctl status ac-control.service

Log data is created in `/var/log/ac-control/`

## How to test

After installation, run the following pytest for integration tests

    make run_tests

## How to expose to Internet

Having local control is nice (e.g. for iOS Shortcuts) but it does not work with Google Home or when not being at home.
Thus, exposing of the server to the Internet is needed. Here an example for how to use `ngrok` for that:

1) Create ngrok account on https://dashboard.ngrok.com/get-started/setup
2) Modify `/opt/ngrok/ngrok.yml` and add your `authtoken` according to your account
3) Restart ngrok service via `sudo systemctl restart ngrok` and verify via `sudo systemctl status ngrok` that it is running
4) Figure out public URL for ngrok service via
	a) ngrok website (https://dashboard.ngrok.com/status/tunnels)
	b) by executing `curl --silent http://127.0.0.1:4040/api/tunnels | jq '.tunnels[] | select(.name == "http") | .public_url'`
	c) by requesting http://<ip-address>:5000/getNgrokUrl in the home network
5) Verify that the service is accessible from Internet by accessing https://223c42a91764.ngrok.io/version

Now you can add e.g. an IFTTT or an iOS shortcut which controls your AC from Google Home or from outside.

## TODOs

* [] add more documentation for setup

# Sources

Following links were used for inspiration:

* ngrok documentation -> https://ngrok.com/docs
* ifttt -> https://ifttt.com/home
