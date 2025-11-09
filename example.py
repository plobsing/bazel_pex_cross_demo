# Toy usage of Pendulum - a relatively uncomplicated third-party Python package with platform-specific wheels on PyPI.
# 
# Adapted from examples on https://pendulum.eustace.io/ .

import pendulum

now = pendulum.now("Europe/Paris")
print(f"Now in Europe/Paris: {now}")

# Changing timezone
now.in_timezone("America/Toronto")
print(f"Now in America/Toronto: {now}")

# Default support for common datetime formats
now.to_iso8601_string()
print(f"Now in ISO 8601: {now}")

# Shifting
now.add(days=2)
print(f"Two days from now: {now}")


