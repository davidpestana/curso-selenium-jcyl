from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest


from concurrent.futures import ThreadPoolExecutor

TEST_FILES = [
    'test/test_base_remote_chrome.py',
    'test/test_base_remote_chrome.py', 
    'test/test_base_remote_chrome.py', 
    'test/test_base_remote_chrome.py', 
    'test/test_base_remote_chrome.py'          
]


def run_test(file):
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern=file)
    runner = unittest.TextTestRunner()
    runner.run(suite)

with ThreadPoolExecutor(max_workers=len(TEST_FILES)) as executor:
    futures = [executor.submit(run_test, file) for file in TEST_FILES]
    for future in futures:
        resutl = future.result() # Espera a que cada tarea termine
        print(resutl)
        # if future.exception() is not None:
        #     print("❌ Error en:", resutl.args)
