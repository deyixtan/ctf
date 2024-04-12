# Dropping BOMs - 2
Category: Celistic

## Description
Celestic's development team thanks you for your assistance, but they are concerned that the `netdata` package was only listed in the Magnezone SBOM and not the Electivire SBOM. It is an integral package in their routers, and they would like your help finding other packages that are listed in the Magnezone SBOM but not the Electivire SBOM.

Comparing the two SBOMs, how many packages (based on name) listed in the Magnezone SBOM are NOT listed in the Electivire SBOM?

Note: this is not just `(# of packages in Magnezone) - (# packages in Electivire)` as there are also packages in Electivire SBOM that are not listed in Magnezone SBOM.

*Flag format: number of packages listed in the Magnezone SBOM that were not listed in the Electivire SBOM. Example: **15***

Attachments: [celestic_router_sbom_electivire.spdx.json](attachments/celestic_router_sbom_electivire.spdx.json), [celestic_router_sbom_magnezone.spdx.json](attachments/celestic_router_sbom_magnezone.spdx.json)

## Write-up
- We can use Python to parse both JSON files and determine the number of packages listed in `Magnezone` SBOM but not in `Electivire`.
- First, we create a set and add all the JSON package entries from `Magnezone` SBOM into the set.
- Next, we iterate over each JSON package entry in `Electivire`. For each entry that does not exist in the previously created set, we count it as 1.
- After finishing all the iterations, we can check the count to obtain our flag, which represents the number of packages found, in this case is `61`.
- The [solve.py](solution/solve.py) script automates the entire process mentioned above.

Flag: `61`
