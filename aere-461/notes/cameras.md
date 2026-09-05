# Cameras

## COTS

Commercial-off-the-shelf products

| Camera             | Price | Fidelity | Mass (w/ battery) | Power |
| ------------------ | ----- | -------- | ----------------- | ----- |
| Flywoo Naked Gopro | $700  | 5.3K@60  | 47.5g             | 2S-6S |
| GoPro HERO13       | $400  | 5.3K@60  | 125g              | 5V 2A |

### Considerations

- COTS cameras are cheaper
- 5.3K@60 is very demanding on the firmware, generating a lot of head
  - Additional cooling will be required in vacuum due to a lack of ambient air
  - We will need directional conduction to relatively large radiators
    - We need to calculate this
  - Direct sunlight will make it reach +120C and shadows to -150C
  - We will need to maintain a pressurized region (on top of the radiators)
    - They call this MLI (multilayer insulation)
  - Operation range: -20C to +50C
- Capacitor outgassing
  - Enclosed capacitors will pop
  - Glues will evaporate and make the lenses foggy
- Solar radiation
  - Electronics will not be radiation hardened
  - We lack the expertise to rad-harden the electronics directly so we'll have to fortify the entire PCB

## Space Ready Cameras

| Camera | Price | Fidelity | Mass (w/ battery) | Power |
| ------ | ----- | -------- | ----------------- | ----- |
| 

### Considerations
