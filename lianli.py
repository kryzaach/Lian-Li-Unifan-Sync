#begin

import usb

#find the LianLi-UNI FAN-SL V2-v0.5
dev = usb.core.find(idVendor=0x0cf2, idProduct=0xa105)

i = dev[0].interfaces()[1].bInterfaceNumber

dev.reset()

if dev.is_kernel_driver_active(i):
    try:
        dev.detach_kernel_driver(i)
    except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

#request type
bmRequestType=0x21

#Set Report Request
bRequest=0x09

#Report is output and ID 224
valuedata=0x02e0

#Index
indexdata=0x01

#fan commands
fandata1=[0xe0, 0x20, 0x00, 0x2d]
fandata2=[0xe0, 0x21, 0x00, 0x2d]
fandata3=[0xe0, 0x22, 0x00, 0x2d]
fandata4=[0xe0, 0x23, 0x00, 0x2d]
fandata5=[0xe0, 0x10, 0x62, 0x11]
fandata6=[0xe0, 0x10, 0x62, 0x22]
fandata7=[0xe0, 0x10, 0x62, 0x44]
fandata8=[0xe0, 0x10, 0x62, 0x88]


#light command
lightdata1=[0xe0, 0x10, 0x61, 0x01]

#termination string
enddata1=[0xe0, 0x50]


#sync everything
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata1)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata2)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata3)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata4)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata5)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata6)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata7)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=fandata8)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=enddata1)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=lightdata1)
result=dev.ctrl_transfer(bmRequestType,bRequest,wValue=valuedata,wIndex=indexdata,data_or_wLength=enddata1)

