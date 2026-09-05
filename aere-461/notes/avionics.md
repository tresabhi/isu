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

| Camera     | Price          | Fidelity | Mass (w/ battery)   | Power |
| ---------- | -------------- | -------- | ------------------- | ----- |
| Astro 3265 | $5000 - $15000 | 9.3K@71  | 450 grams (no lens) | 8W+   |

### Considerations

- I could find just 1 camera that meets our requirements
  - The others were much higher resolution and very low framerates
- Let's not do this one
  - Not only is it hella expensive, but we'd be missing out on all the other cool radiators we'd have to make
  - Also they don't come with lenses by default

# Microcontrollers

| Controller                                     | Price |
| ---------------------------------------------- | ----- |
| Defense-Grade AMD Zynq™ UltraScale+™ XQ MPSoCs | $220  |

## Considerations

- Our only real option are FPGAs so we can build fault tolerant right into the firmware

# Custom Setup

Idk what the hell is going on here but I have some notes

1. Sensor: Sony IMX677 (5.6K@60 -> MIPI lanes)
2. Lane mapping: Mezzanine Card (MIPI lanes -> FPGA pins)
3. Encoder: AMD Zynq™ UltraScale+™ MPSoC ZCU106 Evaluation Kit (10Gbps -> H.264/H.265 -> 50Mbps)
4. Transceiver: Doodle Labs Industrial Wi-Fi Transceivers
