import sys

def error_message_details(err, err_detail:sys):
    _,_,exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_message = 'Error occurred at line=[{0}] name=[{1}] error message=[{2}]'.format(
        exc_tb.tb_lineno, 
        file_name,
        str(err)
    )


class CustomException(Exception):
    def __init__(self, err_message, err_detail:sys):
        super().__init__(err_message)
        self.err_message=error_message_details(err_message, err_detail)

    def __str__(self):
        return self.err_message