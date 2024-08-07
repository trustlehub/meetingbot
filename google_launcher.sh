#!/bin/bash 
PULSE_SINK=chrome_sink xvfb-run --listen-tcp --server-num=18 --auth-file=/tmp/xvfb.auth -s "-ac -screen 0 1920x1080x24" python -m src.meeting.googlebot https://meet.google.com/ysf-yeax-oof 18 ws://localhost:7000 testid
