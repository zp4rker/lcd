#!/bin/bash

cd /home/zp4rker/lcd
runuser -l zp4rker "git reset --hard"
runuser -l zp4rker "git pull"
python3 main.py &
