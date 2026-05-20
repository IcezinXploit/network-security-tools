# Network Security Tools & Auditing Lab

A collection of lightweight Python scripts and utilities designed for network security auditing, port scanning, and local penetration testing sandbox environments. 

## 🚀 Features
* **Multi-threaded Port Scanner**: Fast and efficient TCP port scanner using Python's `concurrent.futures`.
* **Custom Target Selection**: Easily configurable for localhost (`127.0.0.1`) or specific testing subnets.
* **Low Footprint**: Standard library implementation with no heavy external dependencies.

## 🛠️ Requirements
* Python 3.x
* Standard libraries: `socket`, `sys`, `concurrent.futures`, `datetime`

## 📖 Usage

To run the multi-threaded port scanner, execute the following command in your terminal:

```bash
python3 port_scanner.py
