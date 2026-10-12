# RCON hardening

Bind RCON to loopback or a private management interface. Restrict inbound access with a host firewall, use a unique high-entropy password from a secret manager, rotate it after staff changes, and never expose port 25575 to the public internet. RCON is not encrypted in transit; use a VPN or SSH tunnel across untrusted networks.
