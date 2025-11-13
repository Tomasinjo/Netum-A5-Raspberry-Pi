### Intructions
1. Connect Netum A5 to Raspberry Pi
2. Put Netum A5 to Serial mode by scanning [this "USB Serial" QR code](https://www.manualslib.com/manual/3406048/Netum-A5-Nsa5.html#usb-serial)
3. On Raspberry Pi:
    - install pip: `sudo apt install python3-pip`
    - copy the script `netum_a5_barcode.py` to directory of choice
    - create a new venv: `python -m venv venv`
    - activate venv: `source venv/bin/activate`
    - install pyserial: `pip install pyserial`
    - run the script: `python3 netum_a5_barcode.py`
      (if you get a permission error, run with sudo or add yourself to correct group: `sudo usermod -a -G dialout $USER` and try again)
4. Scan the code, the script will output the code.
