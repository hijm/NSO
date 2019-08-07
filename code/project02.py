import ncs
import sys
class requirements():
    def __init__(self):
        self.service_name = raw_input("Service Name: ")
        self.device = raw_input("Device Name: ")
        self.int_id = raw_input("Interface ID: ")
        self.description = raw_input("Description: ")
        self.duplex = raw_input("Duplex: ")
        self.mtu = raw_input("MTU: ")
        self.address = raw_input("IP Address: ")
        self.mask = raw_input("Netmask: ")

def configure_service_intf (service_name,device,int_id,description,duplex,mtu,address,mask):
    with ncs.maapi.single_write_trans('admin', 'python', ['ncsadmin']) as trans:
        root = ncs.maagic.get_root(trans)
        print (root)
        service_entry = root.services.project02.create(service_name)
        service_entry.device = device
        print (service_name,device,int_id,description,duplex,mtu,address,mask)
        Int = service_entry.ios.intf.create(str(int_id))
        print (Int)
        #Int = service_entry.ios.intf.description.create(str(description))
        #Int.intf_id = str(int_id)
        #Int.description = str(description)
        #Int.duplex = str(duplex)
        #Int.mtu = int(mtu)
        #Int.address = str(address)
        #Int.mask = str(mask)
        trans.apply()

newobj = requirements()
configure_service_intf(newobj.service_name,newobj.device,newobj.int_id,newobj.description,newobj.duplex,newobj.mtu,newobj.address,newobj.mask)

