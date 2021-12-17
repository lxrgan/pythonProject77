# -*- coding: utf-8 -*-
#被测试方法
import unittest


class Search:
    def search_fun(self):
        print("search")
        return True
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass search")
        cls.search=Search()
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass search")
    def test_search1(self):
        print("search1")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_search2(self):
        print("search2")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_search3(self):
        print("search3")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断1==1")
    def test_notequal(self):
        print("不相等")
        self.assertNotEqual(1,2,"判断1==2")
        # self.assertTrue(1==1,"ver")



class TestSearch2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass search")
        cls.search=Search()
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass search")
    def test_search21(self):
        print("search21")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_search22(self):
        print("search22")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_search23(self):
        print("search23")
        # search=Search()
        assert  True==self.search.search_fun()
    def test_equal2(self):
        print("断言相等")
        self.assertEqual(1,1,"判断1==1")
    def test_notequa2l(self):
        print("不相等")
        self.assertNotEqual(1,2,"判断1==2")
        # self.assertTrue(1==1,"ver")

if __name__=='__main__':
    #方法一 执行当前文件所有的unittest测试用例
    # unittest.main()
    #方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行
    #创建一个测试套件，testsuie
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search3"))
    # suite.addTest(TestSearch("test_search1"))
    # unittest.TextTestRunner().run(suite)

    #方法三：执行某个测试类
    suite1=unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite2=unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite=unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)