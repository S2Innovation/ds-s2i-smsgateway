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
        # mandatory=True
    )

    PIN = device_property(
        dtype='str',
    )

    # ----------
    # Attributes
    # ----------

    TextMessage = attribute(
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
        self.get_device_properties()
        self._phone = '+48519078083'
        self._textmessage = 'Example Text Message'

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
            self.url = url
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

    def write_TextMessage(self, value):
        # PROTECTED REGION ID(SMSGateway.TextMessage_write) ENABLED START #

        #SMS Max length is 160.
        if len(value) > 160:
            value = value[:160]
        # Check that a sms contains only ASCII characters

        if not(all(ord(char) < 128 for char in value)):
            logging.error('Non-ASCII characters', traceback.format_exc())
            # Remove anything non-ASCII
            value = ''.join([i if ord(i) < 128 else ' ' for i in value])
            self._textmessage = value
            return self._textmessage

        # PROTECTED REGION END #    //  SMSGateway.TextMessage_write

    def write_Phone(self, value):
        # PROTECTED REGION ID(SMSGateway.Phone_write) ENABLED START #
        import re
        # Remove ' ', '-' from number
        value = ''.join([i if i not in [' ', '-'] else '' for i in value])

        # '0048511049007' => '+48511049007'
        if value[:2] == '00':
            value = '+' + value[2:]

        # International number
        def isValidInt(s):
            Pattern = re.compile("^\+(\d{2}\d{3}\d{3}\d{3})")
            return Pattern.match(s)

        def isValid(s):
            Pattern = re.compile("^(\d{3}\d{3}\d{3})")
            return Pattern.match(s)

        if isValidInt(value) or isValid(value):
            self._phone = value
            return self._phone

            # PROTECTED REGION END #    //  SMSGateway.Phone_write

    # --------
    # Commands
    # --------
    @command(
    )
    @DebugIt()
    def SendSMS(self):
        # PROTECTED REGION ID(SMSGateway.SendSMS) ENABLED START #

        print('Phone {0} and SMS {1}'.format(self._phone, self._textmessage))
        # try:
        #     message = self.url + '/manualSMSRefresh.htm?Phone=' + self.Phone + '&SMSContent=' + self.TextMessage
        #     send = requests.get(message)
        #     send.raise_for_status()
        #     self.set_state(PyTango.DevState.ON)
        #     self.set_status('Message sent')
        # except socket.error:
        #     self.set_state(PyTango.DevState.UNKNOWN)
        #     self.set_status('Message NOT sent')
        #     logging.error('Message NOT sent', traceback.format_exc())


        # PROTECTED REGION END #    //  SMSGateway.SendSMS

    @DebugIt()
    def SetPin(self):
        # PROTECTED REGION ID(SMSGateway.SendSMS) ENABLED START #

        #http://192.168.127.254/Set.htm?mode=2&opmode=2&pin=&Band=11&Submit=Submit&setfunc=Cellular
        try:
            message = self.url + '/Set.htm?mode=2&opmode=2&pin=' + str(self.PIN) + '&Band=11&Submit=Submit&setfunc=Cellular'
            send = requests.get(message)
            send.raise_for_status()
            self.set_state(PyTango.DevState.ON)
            self.set_status('PIN updated')
        except socket.error:
            self.set_state(PyTango.DevState.UNKNOWN)
            self.set_status('Pin NOT updated')
            logging.error('Pin NOT updated', traceback.format_exc())

        # PROTECTED REGION END #    //  SMSGateway.SendSMS


    @command(
    )
    @DebugIt()
    def Reset(self):
        # PROTECTED REGION ID(SMSGateway.Reset) ENABLED START #

        #http://192.168.127.254/SaveRestart.htm?
        try:
            message = self.url + '/SaveRestart.htm?'
            send = requests.get(message)
            send.raise_for_status()
            self.set_state(PyTango.DevState.ON)
            self.set_status('Gateway restarted')
        except socket.error:
            self.set_state(PyTango.DevState.UNKNOWN)
            self.set_status('Gateway NOT restarted')
            logging.error('Gateway NOT restarted', traceback.format_exc())

        # PROTECTED REGION END #    //  SMSGateway.Reset

    @command(
    )
    @DebugIt()
    def Connect(self):
        # PROTECTED REGION ID(SMSGateway.Connect) ENABLED START #

        #http://192.168.127.254/Set.htm?mode=2&opmode=0&pin=&Band=11&Submit=Submit&setfunc=Cellular
        try:
            message = self.url + '/Set.htm?mode=2&opmode=0&pin=' + str(self.PIN) + '&Band=11&Submit=Submit&setfunc=Cellular'
            send = requests.get(message)
            send.raise_for_status()
            self.set_state(PyTango.DevState.ON)
            self.set_status('Message sent')
        except socket.error:
            self.set_state(PyTango.DevState.UNKNOWN)
            self.set_status('Message NOT sent')
            logging.error('Message NOT sent', traceback.format_exc())

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
