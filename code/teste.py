from __future__ import print_function
from configure_tunnels_test import create_service_Tunnels_on_device
from sync_from_device import sync_from_device
from wae_file_parser import parse_wae_file
import ncs
import sys
import time

if __name__ == "__main__":
    current_date_and_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    input_file = sys.argv[1] # 1 argument expected (path to WAE file)
    tunnels_dryrun_output = ""
    #rsvp_dryrun_output = ""

    # 1) Parse WAE
    filtered_list_of_devices = parse_wae_file(input_file)

    # 2) Connection Check (WAE Devices)
    #filtered_list_of_devices = remove_disconnected_devices(filtered_list_of_devices)

    # 3) Sync-from (WAE Devices)
    #for device in filtered_list_of_devices:
    #    sync_from_device(device)

    # 4) Tunnels Service (WAE Devices - per Device) 
    for hostname, tunnels in filtered_list_of_devices.items():
        tunnels_dryrun_output = tunnels_dryrun_output + \
            create_service_Tunnels_on_device(hostname, tunnels)

    # 5) Write dry-run Tunnels File
    #tunnels_dryrun_file = "../Output/" + current_date_and_time + "_Tunnels_dry-run.txt"
    #with open(tunnels_dryrun_file, "w") as outfile:
    #    outfile.write(tunnels_dryrun_output)

    # 6) Get Devices with RSVP Configured

    #ios_rsvp_devices = get_ios_devices()
    #xr_rsvp_devices = get_xr_devices()

    # 7) Connection Check (RSVP Devices)
    #ios_rsvp_devices = remove_disconnected_devices(ios_rsvp_devices)
    #xr_rsvp_devices = remove_disconnected_devices(xr_rsvp_devices)

    # 8) Get Target Interfaces on RSVP Devices
    #ios_rsvp_devices_and_interfaces = get_interfaces_ios(ios_rsvp_devices)
    #xr_rsvp_devicess_and_interfaces = get_interfaces_xr(xr_rsvp_devices)

    """
    # 9) Consolidate RSVP Devices and Interfaces
    combined_rsvp_devices_and_interfaces = {}
    combined_rsvp_devices_and_interfaces.update(ios_rsvp_devices_and_interfaces)
    combined_rsvp_devices_and_interfaces.update(xr_rsvp_devicess_and_interfaces)

    # 10) Sync-from (RSVP Devices)
    #for device in combined_rsvp_devices_and_interfaces:
        #sync_from_device(device)

    # 11) RSVP Service (RSVP Devices)
    for hostname, interfaces in combined_rsvp_devices_and_interfaces.items():
        rsvp_dryrun_output = rsvp_dryrun_output + \
            create_service_RSVP_Percentage_on_device(hostname, interfaces, 90)

    # 12) Write dry-run RSVP File
    rsvp_dryrun_file = "../Output/" + current_date_and_time + "_RSVP_Percentage_dry-run.txt"
    with open(rsvp_dryrun_file, "w") as outfile:
        outfile.write(rsvp_dryrun_output)
    """
