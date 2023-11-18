from flask import Flask, request, jsonify

class https_exception(Exception):
    def __init__(self, error_code, message):
        super().__init__(message)
        self.error_code = error_code
        
class not_found_exception(https_exception):
    def __init__(self, message):
        super().__init__(404,message)
        
class bad_request_exception(https_exception):
    def __init__(self, message):
        super().__init__(400,message)

class bad_query_exception(https_exception):
    def __init__(self, message):
        super().__init__(500,message)

class good_result_request():
    def __init__(self, data, status = "success"):
        self.code = 200
        self.status = "success"
        self.data = data


