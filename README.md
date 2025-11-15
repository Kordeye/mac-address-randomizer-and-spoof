# mac-address-randomizer-and-spoof
This application generates randomized or vendor-spoofed MAC addresses. It can create normal random MACs or spoof MACs from well-known brands like Apple, Samsung, Intel, Huawei, and Sony. The app is fast, lightweight, and does not require installation.

How to Use:

1. Open MAC Address Randomizer.exe

2. Under “Spoofing Options,” choose the type of MAC address you want:

Normal Random MAC Address

Apple MAC Address

Samsung MAC Address

Intel MAC Address

Huawei MAC Address

Sony MAC Address

3. Click the Randomize button to generate a MAC address

4. The generated MAC will appear in the center of the window

5. Click the Copy button to copy it to your clipboard

6. A green confirmation message appears when you select an option or copy a MAC address

How It Works:

- Normal Random MAC Address generates a locally administered, unicast MAC address suitable for privacy.

- Brand spoofing modes use real manufacturer prefixes (OUIs). The final three bytes are randomized, creating realistic MAC addresses that resemble real hardware from Apple, Samsung, Intel, Huawei, and Sony.

Requirements:

- Windows 10 or Windows 11

- No installation required

- No administrator permissions required

Safety Information:
This application does not change your actual MAC address. It only generates MACs. To apply a MAC address, you must manually enter it in your network adapter’s settings.

How To Change MAC Address On PC:
1.	Press Win + R, type devmgmt.msc
2.	Network adapters → right-click your Ethernet adapter → Properties
3.	Go to Advanced tab
4.	Look for:
“Locally Administered Address”
or
“Network Address”
5.	Select it → choose Value
6.	Enter a new 12-digit hex number (examples: 3e:cd:1b:a6:f6:c1 is written as 3ECD1BA6F6C1,e2:24:c2:e4:79:03 is written as E224C2E47903)
7.	Click OK
8.	Disable/re-enable the adapter or restart


Credits:
Created by Kordeye
