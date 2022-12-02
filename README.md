# falco-drivers

Checks for new x86_64 AmazonLinux2 kernels hourly and builds falco drivers using Github Actions. Uploads the drivers to https://drivers-falco.s3.amazonaws.com/

Uses code from [Falco Driverkit](https://github.com/falcosecurity/driverkit), [Kernel Crawler](https://github.com/falcosecurity/kernel-crawler), and [Falco test-infra](https://github.com/falcosecurity/test-infra)