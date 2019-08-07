from __future__ import print_function
#from devices_connection_status import remove_disconnected_devices
from wae_file_parser import parse_wae_file
import ncs
import sys
import time

def create_service_Tunnels_on_device(hostname, tunnels):
    with ncs.maapi.single_write_trans('admin', 'python', ['ncsadmin']) as trans:
        root = ncs.maagic.get_root(trans)
        service_name = "Tunnels_" + hostname
        service_entry = root.services.Tunnels.create(service_name)
        print("Creating service Tunnels: " + service_name)
        service_entry.device = hostname
        for tun_id, avg_k in tunnels.items():
            if hostname.upper().startswith("R"):
                print("Configuring tunnel " + str(tun_id) + " with avg_k " + str(int(avg_k)))
                tun = service_entry.ios.tunnels.create(str(tun_id))
                print("punto 1")
                print (int(tun_id))
                #tun.tunnel_id = int(tun_id)
                print("punto 2") 
                tun.avg_kbps = int(avg_k)
            else:
                print("Configuring tunnel " + str(tun_id) + " with avg_k " + str(int(avg_k)))
                tun = service_entry.iosxr.tunnels.create(str(tun_id))
                tun.tunnel_id = int(tun_id)
                tun.avg_kbps = int(avg_k)

        # Dump commit dry run output
        outformat = 'native'
        dryRun = root.services.commit_dry_run
        dryInput = dryRun.get_input()
        dryInput.outformat = outformat
        dryOutput = dryRun(dryInput)
        dryrun_output =  "../Output/" + "_DryRun.txt"
        for d in dryOutput.native.device:
            dryrun_output = dryrun_output + "\n" + d.name + "\n" + d.data.lstrip()

        # Commit
        trans.apply()
        # Return dryrun_output
        return dryrun_output

if __name__ == "__main__":
    current_date_and_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    input_file = sys.argv[1]
    dryrun_file = "./" + current_date_and_time + "_DryRun.txt"
    print(dryrun_file)

    # Use wae_file_parser to get the dictionary of target devices
    filtered_list_of_devices = parse_wae_file(input_file)

    filtered_list_of_devices = remove_disconnected_devices(filtered_list_of_devices)

    total_dryrun_output = ""

    for hostname, tunnels in filtered_list_of_devices.items():
        total_dryrun_output = total_dryrun_output + \
            create_service_Tunnels_on_device(hostname, tunnels)

    with open(dryrun_file, "w") as outfile:
        outfile.write(total_dryrun_output)
