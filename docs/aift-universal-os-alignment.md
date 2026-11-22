# chktex — Optional AIFT Universal OS Developer/Application Integration

> **AIFT planning supplement only; not a change to upstream project authority, licensing, current architecture or shipped AIFT functionality.** The proposed platform and visual infographics are under review in [AIFT-OS PR #92](https://github.com/AIFreedomTrustFederation/AIFT-OS/pull/92).

## Current source role

Upstream GNU GPL licensed LaTeX linting utility, not an OS kernel, preboot environment, robotics runtime or core AIFT federation authority.

## Possible optional integration

Optional developer/build tool in a future AIFT authoring or publishing application; inclusion must retain GNU GPL obligations, software attribution, supported build requirements and actual lint diagnostics.

~~~mermaid
flowchart LR
  UPSTREAM["chktex: existing upstream role"] --> ADAPTER["Opt-in, separately reviewed build/app adapter"]
  ADAPTER -. "only after real tests" .-> AIFT["AIFT development or creative workspace"]
  LIC["License, provenance and author approvals"] --> ADAPTER
  CI["Exact source and target verification"] --> ADAPTER
~~~

## Verifiable acceptance

1. Read existing project README, contribution/agent guide and source license before any implementation.
2. Document any future versioned manifest and environment-specific limitations.
3. Prove Tool build from Autotools source on approved development environment, license review, known-good/known-bad LaTeX fixture, output/exit status and reproducible dependency pins.
4. Keep test/build/publishing and authorization evidence with exact source/artifact SHAs.
5. If not actually installed or executed, label this integration UNVERIFIED and avoid advertising bundled software or a supported hardware OS.

## Non-negotiable boundary

Never replace the upstream README/manual, rebrand it as an AIFT OS component, claim perfect LaTeX validation or silently bundle into a proprietary image. No production deployment, firmware flashing, boot entry changes, hidden telemetry, phone/robot action, security-policy revision or credential handling is part of this document.

See [AIFT-OS draft architecture](https://github.com/AIFreedomTrustFederation/AIFT-OS/pull/92).
