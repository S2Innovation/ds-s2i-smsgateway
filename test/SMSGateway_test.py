#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the SMSGateway project
#
#
#
# Distributed under the terms of the MIT license.
# See LICENSE.txt for more info.
"""Contain the tests for the SMSGateway for PANIC."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from SMSGateway import SMSGateway

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class SMSGatewayDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(SMSGateway.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  SMSGateway.test_additionnal_import
    device = SMSGateway
    properties = {'IP': '', 'PIN': '', 
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SMSGateway.numpy = MagicMock()
        # PROTECTED REGION ID(SMSGateway.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SMSGateway.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(SMSGateway.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SMSGateway.test_properties
        pass

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(SMSGateway.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  SMSGateway.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(SMSGateway.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  SMSGateway.test_Status

    def test_Reset(self):
        """Test for Reset"""
        # PROTECTED REGION ID(SMSGateway.test_Reset) ENABLED START #
        self.device.Reset()
        # PROTECTED REGION END #    //  SMSGateway.test_Reset

    def test_Connect(self):
        """Test for Connect"""
        # PROTECTED REGION ID(SMSGateway.test_Connect) ENABLED START #
        self.device.Connect()
        # PROTECTED REGION END #    //  SMSGateway.test_Connect

    def test_SendSMS(self):
        """Test for SendSMS"""
        # PROTECTED REGION ID(SMSGateway.test_SendSMS) ENABLED START #
        self.device.SendSMS
        # PROTECTED REGION END #    //  SMSGateway.test_SendSMS

    def test_Phone(self):
        """Test for Phone"""
        # PROTECTED REGION ID(SMSGateway.test_Phone) ENABLED START #
        self.device.Phone
        # PROTECTED REGION END #    //  SMSGateway.test_Phone


# Main execution
if __name__ == "__main__":
    main()
