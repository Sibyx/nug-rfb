import unittest

from rfb.core.fields import String, UnsignedInt8
from rfb.core.frames import Frame


class TestFrames(unittest.TestCase):
    def test_simple(self):
        class MyFrame(Frame):
            message_type = String("")
            small_number = UnsignedInt8("")
