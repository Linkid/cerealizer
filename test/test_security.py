#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cerealizer
# Copyright (C) 2005-2006 Jean-Baptiste LAMY
#
# This program is free software.
# It is available under the Python licence.

import unittest

import cerealizer


class TestSecurity(unittest.TestCase):

    def test_register1(self):
        class Sec1: pass
        self.assertRaises(cerealizer.NonCerealizableObjectError, lambda: cerealizer.dumps(Sec1()))

    def test_register2(self):
        class Sec2: pass
        cerealizer.register(Sec2)
        self.assertRaises(ValueError, lambda: cerealizer.register(Sec2))

    def test_register3(self):
        class Sec3: pass
        cerealizer.register(Sec3)
        class Sec3: pass
        self.assertRaises(ValueError, lambda: cerealizer.register(Sec3))

    def test_setstate_hacked(self):
        class Sec4: pass
        cerealizer.register(Sec4)
        o = Sec4()
        Sec4.__setstate__ = lambda obj, state: self.fail()
        cerealizer.loads(cerealizer.dumps(o))

    def test_getstate_hacked(self):
        class Sec5: pass
        cerealizer.register(Sec5)
        o = Sec5()
        Sec5.__getstate__ = lambda obj: self.fail()
        cerealizer.loads(cerealizer.dumps(o))

    def test_new_hacked(self):
        class Sec6: pass
        cerealizer.register(Sec6)
        o = Sec6()
        Sec6.__new__ = lambda Class: self.fail()
        cerealizer.loads(cerealizer.dumps(o))

    def test_craked_file1(self):
        craked_file = "cereal1\n2\n__builtin__.dict\nfile\n0\nr0\nr1\n"
        #self.assertRaises(StandardError, lambda: cerealizer.loads(craked_file))
        self.assertRaises(Exception, lambda: cerealizer.loads(craked_file))
