import unittest
from lsm import LocalStorageMock


class TestLocalStorageMock(unittest.TestCase):
    def test_constructor(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.store, {})
        self.assertEqual(lsm.length, 0)


    def test_key(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.key(0), None)

        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.key(0), 'testkey')

        self.assertEqual(lsm.key(1), None)

        lsm.set_item('testkey2', 'testvalue2')
        self.assertEqual(lsm.key(1), 'testkey2')


    def test_key_non_argument(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.key(0), None)

        lsm.set_item('testkey', 'testvalue')
        with self.assertRaises(TypeError, msg="key() missing 1 required positional argument: 'n'"):
            lsm.key()

    
    def test_get_item(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.get_item('testkey'), None)

        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')


    def test_get_item_not_exists_key(self):
        lsm = LocalStorageMock()
        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey2'), None)


    def test_get_item_non_argument(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.set_item('testkey', 'testvalue'), None)
        
        with self.assertRaises(TypeError, msg="set_item() missing 2 required positional arguments: 'key' and 'value'"):
            lsm.set_item()

        self.assertEqual(lsm.get_item('testkey'), 'testvalue')


    def test_set_item(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        self.assertEqual(lsm.set_item('testkey', 'testvalue'), None)
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')

        self.assertEqual(lsm.set_item('testkey2', 'testvalue2'), None)
        self.assertEqual(lsm.length, 2)
        self.assertEqual(lsm.get_item('testkey2'), 'testvalue2')


    def test_set_item_override_with_same_key(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        self.assertEqual(lsm.set_item('testkey', 'testvalue'), None)
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')

        self.assertEqual(lsm.set_item('testkey', 'testvalue2'), None)
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), 'testvalue2')


    def test_set_item_override_with_same_key_2(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        self.assertEqual(lsm.set_item('testkey', 'testvalue'), None)
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')

        self.assertEqual(lsm.set_item('testkey', ''), None)
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), '')


    def test_set_item_not_specify_key(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        self.assertEqual(lsm.set_item('', 'testvalue'), None)
        self.assertEqual(lsm.length, 0)


    def test_set_item_none_key(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        self.assertEqual(lsm.set_item(None, 'testvalue'), None)
        self.assertEqual(lsm.length, 0)


    def test_set_item_non_argument(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        with self.assertRaises(TypeError, msg="set_item() missing 2 required positional arguments: 'key' and 'value'"):
            lsm.set_item()


    def test_set_item_1_argument(self):
        lsm = LocalStorageMock()
        self.assertEqual(lsm.length, 0)

        with self.assertRaises(TypeError, msg="set_item() missing 2 required positional arguments: 'key' and 'value'"):
            lsm.set_item('testkey')


    def test_remove_item(self):
        lsm = LocalStorageMock()
        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.remove_item('testkey'), None)

        self.assertEqual(lsm.length, 0)
        self.assertEqual(lsm.get_item('testkey'), None)


    def test_remove_item_not_exists_key(self):
        lsm = LocalStorageMock()
        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.remove_item('testkey2'), None)

        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')


    def test_remove_item_already_deleted_key(self):
        lsm = LocalStorageMock()
        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')
        self.assertEqual(lsm.length, 1)
        self.assertEqual(lsm.remove_item('testkey'), None)

        self.assertEqual(lsm.length, 0)
        self.assertEqual(lsm.get_item('testkey'), None)

        self.assertEqual(lsm.remove_item('testkey'), None)


    def test_remove_item_non_argument(self):
        lsm = LocalStorageMock()
        with self.assertRaises(TypeError, msg="remove_item() missing 1 required positional argument: 'key'"):
            lsm.remove_item()


    def test_clear(self):
        lsm = LocalStorageMock()
        lsm.set_item('testkey', 'testvalue')
        self.assertEqual(lsm.get_item('testkey'), 'testvalue')
        self.assertEqual(lsm.length, 1)

        self.assertEqual(lsm.clear(), None)
        self.assertEqual(lsm.get_item('testkey'), None)
        self.assertEqual(lsm.length, 0)


if __name__ == "__main__":
    unittest.main()
