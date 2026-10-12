# mc-rcon-operator-cli

A small Python CLI for explicit, auditable RCON commands. It is intended for trusted operators on private networks, not as a public HTTP control plane.

## Safety
- Requires an explicit command; no implicit destructive actions.
- Reads credentials from environment variables, never command-line arguments.
- Uses a connection timeout and does not log the password.
- Restrict RCON to loopback/private network and firewall it to operator hosts.

## Run
Set `MC_RCON_HOST`, `MC_RCON_PORT`, and `MC_RCON_PASSWORD`, then `python3 rconctl.py list`. Review and test before sending mutation commands. MIT licensed.
