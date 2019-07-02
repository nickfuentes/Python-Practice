
import unittest  # import unittest module 
# import Task class in the unit test file 
from task import Task 

 #unittest is module name
 # TestCase is the class name which contains all the unit test functions 
class TodoListTestCase(unittest.TestCase):

    def test_should_be_able_to_add_task_to_list(self): 
        tasks = [] 
        task = Task("Wash the car")
        tasks.append(task)
        tasks.append(task)
        self.assertEqual(1,len(tasks))


    # test function should always begin with test string 
    def test_should_be_able_to_create_task(self): 
        #self.assertEqual(2, 5)
        # creating a task object 
        task = Task("Wash the car")
        # asserting that task is not null/none 
        self.assertIsNotNone(task)

# run the test 
unittest.main()

