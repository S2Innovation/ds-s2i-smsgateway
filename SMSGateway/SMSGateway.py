# -*- coding: utf-8 -*-
#
# This file is part of the SMSGateway project
#
#
#
# Distributed under the terms of the MIT license.
# See LICENSE.txt for more info.

""" SMSGateway for PANIC

"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(SMSGateway.additionnal_import) ENABLED START #
import requests
import socket
import traceback
import logging

# PROTECTED REGION END #    //  SMSGateway.additionnal_import

__all__ = ["SMSGateway", "main"]


class SMSGateway(Device):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(SMSGateway.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SMSGateway.class_variable

    # -----------------
    # Device Properties
    # -----------------

    IP = device_property(
        dtype='str',
        mandatory=True
    )

    PIN = device_property(
        dtype='str',
    )

    # ----------
    # Attributes
    # ----------

    SendSMS = attribute(
        dtype='str',
        access=AttrWriteType.WRITE,
        doc="SMS content, Max length is 160.",
    )

    Phone = attribute(
        dtype='str',
        access=AttrWriteType.WRITE,
        doc="SMS Receiveer",
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(SMSGateway.init_device) ENABLED START #
        addr = str(self.IP)
        try:
            socket.inet_aton(addr)
            url = 'http://' + addr
        except socket.error:
            self.set_state(PyTango.DevState.UNKNOWN)
            self.set_status('Invalid IP address')
            logging.error('Invalid IP address', traceback.format_exc())

        try:
            test_connection = requests.get(url)
            test_connection.raise_for_status()
            self.set_state(PyTango.DevState.ON)
            self.set_status('Connected with SMS Gatway')
        except socket.error:
            self.set_state(PyTango.DevState.UNKNOWN)
            self.set_status('Bad request made, a 4XX client error or 5XX server error response')
            logging.error('Bad request made, a 4XX client error or 5XX server error response', traceback.format_exc())

        # PROTECTED REGION END #    //  SMSGateway.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(SMSGateway.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(SMSGateway.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def write_SendSMS(self, value):
        # PROTECTED REGION ID(SMSGateway.SendSMS_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.SendSMS_write

    def write_Phone(self, value):
        # PROTECTED REGION ID(SMSGateway.Phone_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.Phone_write


    # --------
    # Commands
    # --------

    @command(
    )
    @DebugIt()
    def Reset(self):
        # PROTECTED REGION ID(SMSGateway.Reset) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.Reset

    @command(
    )
    @DebugIt()
    def Connect(self):
        # PROTECTED REGION ID(SMSGateway.Connect) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SMSGateway.Connect

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(SMSGateway.main) ENABLED START #
    return run((SMSGateway,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SMSGateway.main

if __name__ == '__main__':
    main()
