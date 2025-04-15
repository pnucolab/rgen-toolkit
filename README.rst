Variant-aware Cas-OFFinder
=========================

This repository provides comprehensive documentation for the Variant-aware Cas-OFFinder tool. 
It includes a detailed user guide for the web interface, instructions for using the command-line interface (CLI), 
and a Docker Compose file for easy local deployment.

Prerequisites
=============

To run the command-line interface or host the web application locally, an OpenCL-compatible device is required. 
OpenCL (Open Computing Language) enables parallel computing across heterogeneous systems and is essential for the
high-performance computational tasks performed by Cas-OFFinder.

System Requirements:
--------------------
• OpenCL-compatible hardware:
   - GPUs (e.g., NVIDIA, AMD)
   - Some CPUs that support OpenCL
• Installed OpenCL drivers for your device
• Docker (for using the docker-compose deployment)
• Python (if using the CLI version outside of Docker)

Tip: You can verify your OpenCL setup using tools like `clinfo`.

Note: While the web-based tool can be accessed remotely (hosted version), running it 
locally or via CLI requires proper OpenCL setup to ensure efficient off-target search performance.


Citations
=========



License
=======

Copyright (C) 2024 Mekonnen Abyot Melkamu and Jeongbin Park

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.
