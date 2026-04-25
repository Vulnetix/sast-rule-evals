# Sample for Ruff rule PLR0913: too-many-arguments
# This file is designed to trigger the PLR0913 rule.
# Run: ruff check --select PLR0913 <this_file>

def calculate_position(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, time):
    new_x = x_pos + x_vel * time
    new_y = y_pos + y_vel * time
    new_z = z_pos + z_vel * time
    return new_x, new_y, new_z
