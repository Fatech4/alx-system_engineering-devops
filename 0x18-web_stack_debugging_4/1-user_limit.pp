# This manifest sets file descriptor limits for the holberton user.
#
# Parameters:
#   - hard: The hard limit for file descriptors.
#   - soft: The soft limit for file descriptors.
user { 'holberton':
  hard => 10000,
  soft => 10000,
}
