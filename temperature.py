#temperature sensor.

with open("/sys/class/thermal/thermal_zone0/temp") as f:
    temp = int(f.read()) / 1000

print(f"CPU Temperature: {temp:.1f}°C")

if temp > 60:
    print("Wowee, it's burning up in here!")
else: #temp is normal
    print("Staying cool!")