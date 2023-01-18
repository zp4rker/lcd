#!/bin/bash

cd /home/zp4rker/lcd
runuser -l zp4rker -c "cd /home/zp4rker/lcd && git reset --hard && git pull"
python3 main.py &
