import os
import sys
import unittest
sys.path.append((os.path.dirname(__file__) or '.') + '/..')

import weechat
from buffer_autohide import *


class TestList(unittest.TestCase):
    def setUp(self):
        self.config_name = "excemptions"
        if not weechat.config_is_set_plugin(self.config_name):
            weechat.config_set_plugin(self.config_name, "")


    def tearDown(self):
        if weechat.config_is_set_plugin(self.config_name):
            weechat.config_unset_plugin(self.config_name)


    def test_list_excemptions(self):
        # no entries
        weechat.config_set_plugin(self.config_name, "")
        self.assertEqual(list_excemptions(), [])

        weechat.config_set_plugin(self.config_name, "{0}".format(DELIMITER))
        self.assertEqual(list_excemptions(), [])

        # one entry
        weechat.config_set_plugin(self.config_name, "foo")
        self.assertEqual(list_excemptions(), ['foo'])
        weechat.config_set_plugin(self.config_name, "{0}foo".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo'])
        weechat.config_set_plugin(self.config_name, "{0}foo{0}".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo'])
        weechat.config_set_plugin(self.config_name, "foo{0}".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo'])

        # two entries
        weechat.config_set_plugin(self.config_name, "foo{0}bar".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo', 'bar'])

        weechat.config_set_plugin(self.config_name, "{0}foo{0}bar".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo', 'bar'])

        weechat.config_set_plugin(self.config_name, "{0}foo{0}bar{0}".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo', 'bar'])

        weechat.config_set_plugin(self.config_name, "{0}foo{0}bar".format(DELIMITER))
        self.assertEqual(list_excemptions(), ['foo', 'bar'])


    def test_add_to_excemptions(self):
        weechat.config_set_plugin(self.config_name, "")
        add_to_excemptions("foo")
        self.assertEqual(list_excemptions(), ['foo'])

        weechat.config_set_plugin(self.config_name, "{0}".format(DELIMITER))
        add_to_excemptions("foo")
        self.assertEqual(list_excemptions(), ['foo'])

        weechat.config_set_plugin(self.config_name, "foo")
        add_to_excemptions("bar")
        self.assertEqual(list_excemptions(), ['foo', 'bar'])

        weechat.config_set_plugin(self.config_name, "{0}foo".format(DELIMITER))
        add_to_excemptions("bar")
        self.assertEqual(list_excemptions(), ['foo', 'bar'])

        weechat.config_set_plugin(self.config_name, "foo{0}".format(DELIMITER))
        add_to_excemptions("bar")
        self.assertEqual(list_excemptions(), ['foo', 'bar'])


    def test_del_from_excemptions(self):
        weechat.config_set_plugin(self.config_name, "foo")
        with self.assertRaises(ValueError):
            del_from_excemptions("bar")

        weechat.config_set_plugin(self.config_name, "foo")
        del_from_excemptions("foo")
        self.assertEqual(list_excemptions(), [])

        weechat.config_set_plugin(self.config_name, "foo{0}".format(DELIMITER))
        del_from_excemptions("foo")
        self.assertEqual(list_excemptions(), [])

        weechat.config_set_plugin(self.config_name, "{0}foo{0}".format(DELIMITER))
        del_from_excemptions("foo")
        self.assertEqual(list_excemptions(), [])

        weechat.config_set_plugin(self.config_name, "{0}foo".format(DELIMITER))
        del_from_excemptions("foo")
        self.assertEqual(list_excemptions(), [])

        weechat.config_set_plugin(self.config_name, "foo{0}bar".format(DELIMITER))
        del_from_excemptions("bar")
        self.assertEqual(list_excemptions(), ['foo'])

        weechat.config_set_plugin(self.config_name, "foo{0}bar".format(DELIMITER))
        self.assertEqual(del_from_excemptions("2"), ['foo'])

        weechat.config_set_plugin(self.config_name, "foo{0}bar".format(DELIMITER))
        with self.assertRaises(IndexError):
            del_from_excemptions("3")


if __name__ == '__main__':
    unittest.main()

