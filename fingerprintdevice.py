from elftools.elf.elffile import ELFFile

with open("14_11_FingerscannerDevice.elf", "rb") as f:
    elf = ELFFile(f)

    print("Architecture:", elf['e_machine'])
    print("Entry point:", hex(elf['e_entry']))

    print("\nSections:")
    for section in elf.iter_sections():
        print(section.name, hex(section['sh_addr']))
