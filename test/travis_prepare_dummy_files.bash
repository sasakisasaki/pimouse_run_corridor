#!/bin/bash -xve

sudo touch /dev/rt{lightsensor,buzzer,motor,motoren,motor_raw_{l,r}}0
sudo chmod 666 /dev/rt{lightsensor,buzzer,motor,motoren,motor_raw_{l,r}}0
echo "0 0 0 0" | sudo tee /dev/rtlightsensor0
echo "0" | sudo tee /dev/rtswitch{0,1,2}
sudo chmod 666 /dev/rtswitch{0,1,2}
