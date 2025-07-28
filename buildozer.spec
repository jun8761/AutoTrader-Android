[app]
title = AutoTrader
package.name = autotrader
package.domain = org.kivy
source.dir = app
source.include_exts = py,json
version = 1.0
requirements = python3,kivy,pyupbit,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.release = True
# Uncomment to enable AAB generation
android.aab = True

[buildozer]
log_level = 2
warn_on_root = 1
p4a.bootstrap = sdl2