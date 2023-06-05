import json

electivireFile = open("../attachments/celestic_router_sbom_electivire.spdx.json", "r")
magnezoneFile = open("../attachments/celestic_router_sbom_magnezone.spdx.json", "r")

electivireContent = electivireFile.read()
magnezoneContent = magnezoneFile.read()

electivirePackagesJson = json.loads(electivireContent)["packages"]
magnezonePackagesJson = json.loads(magnezoneContent)["packages"]

electivirePackagesSet = set()
for package in electivirePackagesJson:
    electivirePackagesSet.add(package["name"])

count = 0
for package in magnezonePackagesJson:
    if package["name"] not in electivirePackagesSet:
        count += 1

print(count)
