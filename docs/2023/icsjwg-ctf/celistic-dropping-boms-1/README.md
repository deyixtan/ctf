# Dropping BOMs - 1
Category: Celistic

## Description
As part of an effort to improve their security posture, Celestic's software development team has been creating software bills of materials (SBOMs) for their in-house developed software. The development team created two different tools to generate SBOMs: **Electivire** and **Magnezone**. Electivire integrates with the developers CI/CD pipeline to create SBOMs based on source code and Magnezone creates SBOMs from the final packages and binaries.

Normally, Electivire and Magnezone produce very similar SBOMs, but in the case of Celestic's internal routers, the two tools produced different results. Additionally, the security team has requested a specific package version and hash.

In these **Dropping BOMs** challenges, you will examine and compare the inconsistent router SBOMs and assist the security team with their requests.

The initial request from Celestic's security team involves the `netdata` package.

Using the attached SBOMs, what is the listed version of the `netdata` package?

*Flag format: netdata version. Example: if the request was for the version of dropbear, the flag would be **2022.82-2***

Attachments: [celestic_router_sbom_electivire.spdx.json](attachments/celestic_router_sbom_electivire.spdx.json), [celestic_router_sbom_magnezone.spdx.json](attachments/celestic_router_sbom_magnezone.spdx.json)

## Write-up
- We can find the `netdata` version from [attachments](attachments/celestic_router_sbom_magnezone.spdx.json) by finding the term `netdata`. The version can be found in the corresponding package's `versionInfo` attribute.

- Open the [celestic_router_sbom_magnezone.spdx.json](attachments/celestic_router_sbom_magnezone.spdx.json) file.
- Search for the term `netdata` in the file.
- Look for the corresponding package entry that mentions `netdata` in the `name` attribute.
- Within the package entry, locate the `versionInfo` attribute.
- The value `1.33.1-2` of the `versionInfo` attribute is the flag.

Flag: `1.33.1-2`
