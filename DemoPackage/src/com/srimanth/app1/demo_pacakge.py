import logging as log


class DemoPackage:
    def __init__(self,file_name):
        self.file_name= file_name

    def health_check(self):
        log.info("Hello This is working")
        return "Hello I am Good"


