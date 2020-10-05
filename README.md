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

	http://<ip-address>:5000/turnOn
	http://<ip-address>:5000/turnOff
	http://<ip-address>:5000/custom?temperature=25&fan=Silent

Example via curl:

	curl -f http://<ip-address>:5000/turn-on

## How to monitor / debug service

To verify the functionality of the service, check

	sudo systemctl status ac-control.service

Log data is created in `/var/log/ac-control/`

## How to test

After installation, run the following pytest for integration tests

    make run_tests

## TODOs

* [] add more documentation for setup

# Sources

Following links were used for inspiration:

TBD
