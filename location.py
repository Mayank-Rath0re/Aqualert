import subprocess
import geocoder

def get_location():
    ip = subprocess.run(["curl","ifconfig.me"],capture_output=True).stdout.decode('ascii')
    print(ip)
    g = geocoder.ip(ip)
    return g.latlng