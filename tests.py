from unittest import TestCase


class TestComposition(TestCase):
    def setUp(self):
        class Superclass(object):
            pass

        class MakeSureWeDidNotLeakState(Superclass):
            pass

    def test_it_causes_inheritance_to_fail(self):
        import composition
        self.addCleanup(composition.demon_worship)

        class Superclass(object):
            pass

        with self.assertRaises(composition.UseIt):
            class Subclass(Superclass):
                pass

        class UnittestStillWorks(TestCase):
            pass
