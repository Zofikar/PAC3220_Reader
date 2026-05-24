## Network Bootstrap & Configuration

This repository includes a `bootstrap.sh` script designed to automate system dependencies, clone the repository cleanly
into user 1000's home directory with proper ownership permissions, and configure an isolated network interface on `eth0`
with a static IP (`192.168.1.99`) and no gateway access.

### Prerequisites

* A Debian/Ubuntu-based Linux distribution.
* Root or `sudo` privileges.

### Quick Install (One-Liner)

If your target machine has temporary internet access and you want to fetch and execute the setup immediately, run:

```bash
curl -sSL https://raw.githubusercontent.com/Zofikar/PAC3220_Reader/main/bootstrap.sh | sudo bash