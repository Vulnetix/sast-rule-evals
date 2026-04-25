# vnx-sec-026 eval target: DigitalOcean personal access token hardcoded
import digitalocean

# TRIGGERS rule
DO_TOKEN = "dop_v1_a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"

manager = digitalocean.Manager(token=DO_TOKEN)
