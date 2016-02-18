import sys, time
from modules.app import App

print time.strftime("%Y-%m-%d %H:%M:%S")

App().start(sys.argv)

print time.strftime("%Y-%m-%d %H:%M:%S")
