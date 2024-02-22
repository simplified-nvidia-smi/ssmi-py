# SSMI - Simplified NVIDIA System Management Interface Tool

`ssmi` is a lightweight command-line tool designed to provide a simplified version of the output from the NVIDIA System Management Interface (`nvidia-smi`). It focuses on displaying GPU and process details more concisely, offering a streamlined overview for quick assessments.

## Features

- Display GPU details, including performance, temperature, power usage, memory usage, and utilization metrics.
- Display process details, listing each process utilizing the GPU, including process ID, type, name, and memory usage.
- Filter output to show only GPU details, only process details, or both.

### Output Differences:

**nvidia-smi**

```
Tue Feb 20 13:40:51 2024
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.154.05             Driver Version: 535.154.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA RTX A5500 Laptop GPU    Off | 00000000:01:00.0 Off |                  Off |
| N/A   47C    P8              16W /  90W |   1206MiB / 16384MiB |     21%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      2241      G   /usr/lib/xorg/Xorg                          492MiB |
|    0   N/A  N/A     14541      G   /usr/bin/kwalletd5                            4MiB |
|    0   N/A  N/A     14722      G   ...-gnu/libexec/xdg-desktop-portal-kde        4MiB |
|    0   N/A  N/A     14766      G   /usr/bin/ksmserver                            4MiB |
|    0   N/A  N/A     14768      G   /usr/bin/kded5                                4MiB |
|    0   N/A  N/A     14771      G   /usr/bin/kwin_x11                           131MiB |
|    0   N/A  N/A     14814      G   /usr/bin/plasmashell                         64MiB |
|    0   N/A  N/A     14847      G   ...c/polkit-kde-authentication-agent-1        4MiB |
|    0   N/A  N/A     15108      G   ...86_64-linux-gnu/libexec/kdeconnectd        4MiB |
|    0   N/A  N/A     15123      G   /usr/bin/kaccess                              4MiB |
|    0   N/A  N/A     15136      G   ...-linux-gnu/libexec/DiscoverNotifier        4MiB |
|    0   N/A  N/A     15138      G   /usr/bin/kalendarac                           4MiB |
|    0   N/A  N/A     15252      G   ...ures=SpareRendererForSitePerProcess        9MiB |
|    0   N/A  N/A     15573      G   /usr/bin/dolphin                              4MiB |
|    0   N/A  N/A     15602      G   /opt/google/chrome/chrome                     4MiB |
|    0   N/A  N/A     15645      G   ...seed-version=20240216-130127.682000      273MiB |
|    0   N/A  N/A     17641      G   /usr/bin/kwalletmanager5                     70MiB |
|    0   N/A  N/A     17899      G   /usr/bin/alacritty                           10MiB |
|    0   N/A  N/A     23102      G   /usr/bin/alacritty                           10MiB |
|    0   N/A  N/A     25803      G   ...AAAAAAAACAAAAAAAAAA= --shared-files       32MiB |
+---------------------------------------------------------------------------------------+
```

**ssmi**

```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.154.05             Driver Version: 535.154.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Fan  Temp  Perf      Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|=========================================+======================+======================|
|   0  N/A   47C   P5          25W /  90W |   1238MiB / 16384MiB |     11%      Default |
+-----------------------------------------+----------------------+----------------------+
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|=======================================================================================|
|    0   N/A  N/A      2241      G   /usr/lib/xorg/Xorg                          511MiB |
|    0   N/A  N/A     14541      G   /usr/bin/kwalletd5                            4MiB |
|    0   N/A  N/A     14722      G   ...-gnu/libexec/xdg-desktop-portal-kde        4MiB |
|    0   N/A  N/A     14766      G   /usr/bin/ksmserver                            4MiB |
|    0   N/A  N/A     14768      G   /usr/bin/kded5                                4MiB |
|    0   N/A  N/A     14771      G   /usr/bin/kwin_x11                           132MiB |
|    0   N/A  N/A     14814      G   /usr/bin/plasmashell                         64MiB |
|    0   N/A  N/A     14847      G   ...c/polkit-kde-authentication-agent-1        4MiB |
|    0   N/A  N/A     15108      G   ...86_64-linux-gnu/libexec/kdeconnectd        4MiB |
|    0   N/A  N/A     15123      G   /usr/bin/kaccess                              4MiB |
|    0   N/A  N/A     15136      G   ...-linux-gnu/libexec/DiscoverNotifier        4MiB |
|    0   N/A  N/A     15138      G   /usr/bin/kalendarac                           4MiB |
|    0   N/A  N/A     15252      G   ...ures=SpareRendererForSitePerProcess        9MiB |
|    0   N/A  N/A     15573      G   /usr/bin/dolphin                              4MiB |
|    0   N/A  N/A     15602      G   /opt/google/chrome/chrome                     4MiB |
|    0   N/A  N/A     15645      G   ...seed-version=20240216-130127.682000      273MiB |
|    0   N/A  N/A     17641      G   /usr/bin/kwalletmanager5                     70MiB |
|    0   N/A  N/A     17899      G   /usr/bin/alacritty                           10MiB |
|    0   N/A  N/A     23102      G   /usr/bin/alacritty                           10MiB |
|    0   N/A  N/A     25803      G   ...AAAAAAAACAAAAAAAAAA= --shared-files       44MiB |
+---------------------------------------------------------------------------------------+
```



## Installation

There are two options for installation

#### Pip
```bash
pip install ssmi-py
```

#### Source
```bash
git clone https://github.com/simplified-nvidia-smi/ssmi-py
cd ssmi-py
sudo make install
```

This will install `ssmi` to `/usr/bin` and its man page to the appropriate system directories.

## Usage

Run `ssmi` without any arguments to display both GPU details and process information.

```bash
ssmi
```

To display only GPU details:

```bash
ssmi -g
```

To display only process details:

```bash
ssmi -p
```

For more information and options, use the help flag:

```bash
ssmi -h
```

## Contributing

Contributions to `ssmi` are welcome! Please feel free to submit pull requests, report bugs, and suggest features through the GitHub issue tracker.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Authors

- Ben Elfner
