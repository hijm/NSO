from __future__ import print_function
import ncs
import sys
import time

def create_service_interface_on_device(hostname, interface_name):
    with ncs.maapi.single_write_trans('admin', 'python', ['ncsadmin']) as trans:
        print(hostname, interface_name)
        root = ncs.maagic.get_root(trans)
        service_name = input("Enter the service name")
        print(service_name)
        service_entry = root.services.project01.create(service_name)
        service_entry.device = hostname

        print("Creating service Interface: " + service_name)
        #tun = service_entry.ios.tunnels.create(str(tun_id))
        #tun.tunnel_id = int(tun_id)
       
        Int = service_entry.ios.interfaces.create(str(interface_name))
        #Int.interface_name = str(interface_name)
        #tun.tunnel_id = int(tun_id)
        
        """
       
        # Dump commit dry run output
        outformat = 'native'
        dryRun = root.services.commit_dry_run
        dryInput = dryRun.get_input()
        dryInput.outformat = outformat
        dryOutput = dryRun(dryInput)
        dryrun_output = "../Output/" + "DryRun.txt"
        for d in dryOutput.native.device:
            dryrun_output = dryrun_output + "\n" + d.name + "\n" + d.data.lstrip()
        """
        # Commit
        trans.apply()
        # Return dryrun_output
        #return dryrun_output

def getValues ():
    enter_interface_name = input("Enter the interface name:")
    enter_hostname = input("Enter the hostname name:")
    create_service_interface_on_device(enter_hostname,enter_interface_name)


if __name__ == "__main__":
    #main()
    getValues()
    """
    current_date_and_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    input_file = sys.argv[1]
    dryrun_file = "../Output/" + current_date_and_time + "_DryRun.txt"
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
    """