# ac-controller

## Objective

The objective of this repo is to have a working python / bash script / program which allows controlling a Mitsubishi AC (model: xxx)

## Raspberry Pi Setup

### Step 1) Buy right hardware parts

TODO

### Step 2) Connect everything

TODO

### Step 3) Configure raspberry pi

Add the following lines to `/boot/config.txt` at the end of the file (order is important)
```
dtoverlay=gpio-ir-tx,gpio_pin=22 # input
dtoverlay=gpio-ir,gpio_pin=23 # output
```

Install lirc via 
```
sudo apt install lirc
```

Reboot
```
sudo reboot
```

### Step 4) Verify receiving of signals
```
pi@rpi2:~ $ mode2 -d /dev/lirc0
Using driver default on device /dev/lirc0
Trying device: /dev/lirc0
Using device: /dev/lirc0
# click
pulse 498
space 345
pulse 440
```

### Step 5) Verify sending of signals
```
irdb-get download streamzap/streamzap.lircd.conf 
cp streamzap.lircd.conf /etc/lirc/lircd.conf.d/
sudo systemctl restart lircd
irsend list Streamzap_PC_Remote KEY_0
irsend send_once Streamzap_PC_Remote KEY_0 # -> check with phone camera, red light should appear
```

### Hints / Known Issues
* seems like input pin does not work anymore when output pin is activated in `/boot/config.txt`


## Tested Approaches

### Approach 1) Record via lircd `irrecord`

How to: Execute `irrecord` and follow steps. Ideally lircd.conf is created which can be replayed

Actual: `irrecord` seems to not work with AC controllers which transmit the full state of the AC

### Approach 2) Record via `mode2 -d /dev/lircd`

From: 

* https://web.archive.org/web/20170201131003/http://absurdlycertain.blogspot.com/2013_03_01_archive.html
* https://github.com/tpudlik/RaspAC
* https://medium.com/@camilloaddis/smart-air-conditioner-with-raspberry-pi-an-odissey-2a5b438fe984

How to: 

1) Execute `mode2 -d /dev/lirc0 > power_on` and receive signals
2) Copy content of `power_on` and execute it as part of `lirc_parser.py` (copy to `/home/bij81sgp/Desktop/recordings` on home device)
3) Copy output to `/etc/lirc/lircd.conf.d/ac.conf`
4) Reload and verify lirc
```
sudo systemctl restart lircd
sudo systemctl status lircd

# show list of commands
irsend LIST mitsubishi_ac power_on

# execute command
irsend SEND_ONCE mitsubishi_ac power_on
```

Actual: No error while sending, but no reaction at AC.

Possible issues:
* Wrong recording from `mode2` or `lirc_parser.py`
* Bad lirc conf header

Steps to try out:
* Verify multiple `mode2` results
* Modify ac.conf header values
    * e.g. from https://stackoverflow.com/questions/30118014/how-to-record-an-ir-signal-from-an-ac-remote-using-lirc-in-raspberry-pi
    * e.g. from https://stackoverflow.com/questions/22652156/how-to-use-irrecord-with-2ms-timing-instead-of-the-default-5ms
* Verify CRC (verification at the end of the signal)

## Approach 3) 

From: 
* https://www.analysir.com/blog/2015/01/06/reverse-engineering-mitsubishi-ac-infrared-protocol/
* https://github.com/r45635/HVAC-IR-Control
* https://github.com/Ericmas001/HVAC-IR-Control (this)

How to:

1) Install right packages
```
sudo apt install git python3-pip python3-setuptools python3-pigpio
# maybe also pip3 install pigpio
```

2) Clone repo
```
cd ~/dev/
git clone https://github.com/Ericmas001/HVAC-IR-Control.git
```

3) Modify GPIO pin to 22 from 23 in `demo_mitsu.py`
```
HVAC = Mitsubishi(22, LogLevel.ErrorsOnly)
```

4) Execute and verify
```
sudo su
cd /home/pi/dev/HVAC-IR-Control/python/hvac_ircontrol/
export PYTHONPATH=.
python3 ../demo_mitsu.py

# verify with camera
```

Actual: No error while sending, but no reaction at AC.

Possible issues:
* Wrong signal from repo
* Too short range for IR sender 

Steps to try out:
* Go closer to AC (get Wi-Fi adapter for raspi / use raspi 3)
* Try to decode actual signals (from `mode2`) and compare them with https://github.com/Ericmas001/HVAC-IR-Control/blob/master/Protocol/Mitsubishi_IR_Packet_Data_v1.1-FULL.pdf / log output from `demo_mitsu.py`

## Approach 4) Rebuilding of kernel

From: https://primus.kot-begemot.co.uk/node/94

How to: TBD