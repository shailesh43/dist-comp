import ntplib
from datetime import datetime
import time


def synchronize_clock(ntp_server="pool.ntp.org"):

    client = ntplib.NTPClient()

    try:
        print(f"Connecting to NTP Server: {ntp_server}\n")

        response = client.request(ntp_server, version=3, timeout=5)
        # Local system time
        system_time = time.time()

        # Time received from NTP server
        ntp_time = response.tx_time

        system_readable = datetime.fromtimestamp(system_time)
        ntp_readable = datetime.fromtimestamp(ntp_time)

        print("Local System Time :", system_readable)
        print("NTP Server Time   :", ntp_readable)

        # Calculate clock offset
        offset = ntp_time - system_time

        print("\nClock Offset:", round(offset, 6), "seconds")

        if abs(offset) < 1:
            print("System clock is almost synchronized.")
        else:
            print("System clock differs from NTP server.")

    except Exception as e:
        print("Error while connecting to NTP server:", e)


if __name__ == "__main__":
    synchronize_clock("time.google.com")