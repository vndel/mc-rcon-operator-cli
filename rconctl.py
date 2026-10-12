#!/usr/bin/env python3
"""Minimal Source RCON query client for trusted Minecraft operators."""
import argparse
import os
import socket
import struct
import sys


def packet(request_id: int, kind: int, body: str) -> bytes:
    payload = struct.pack("<ii", request_id, kind) + body.encode() + b"\0\0"
    return struct.pack("<i", len(payload)) + payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="explicit RCON command to send")
    args = parser.parse_args()
    host = os.environ.get("MC_RCON_HOST", "127.0.0.1")
    port = int(os.environ.get("MC_RCON_PORT", "25575"))
    password = os.environ.get("MC_RCON_PASSWORD")
    if not password:
        parser.error("MC_RCON_PASSWORD must be set in the environment")
    with socket.create_connection((host, port), timeout=3) as sock:
        sock.settimeout(3)
        sock.sendall(packet(1, 3, password))
        response = sock.recv(4096)
        if len(response) < 14:
            raise RuntimeError("short RCON authentication response")
        request_id = struct.unpack("<i", response[4:8])[0]
        if request_id == -1:
            raise PermissionError("RCON authentication rejected")
        sock.sendall(packet(2, 2, args.command))
        data = sock.recv(4096)
        if len(data) < 14:
            raise RuntimeError("short RCON response")
        sys.stdout.write(data[12:-2].decode(errors="replace"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
