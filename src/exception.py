import sys

def error_message_detail(error,error_detail:sys):
    '''
    Generates a detailed error message with script name, line number and error description.

    Parameters:
    error (Exception): The exception instance.
    error_detail (sys): System module used for extract traceback details.

    Returns:
    str: Formatted error message with file name, line number, and error description.
    '''

    # Extract track back object from sys.exc_info()
    _,_,exc_tb = error_detail.exc_info()

    # Get the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Custom error message format
    error_message = "Error occured in python script name: [{0}] \nline number: [{1}] \nerror message: [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message

class CustomException(Exception):
    '''
    Custom exception class to get detailed error message with script name and line number.
    '''

    def __init__(self, error_message, error_detail:sys):
        '''
        Initialize CustomException class with detailed error message.

        Parameters:
        error_message (Exception): The exception instance.
        error_detail (sys): System module use for extract traceback details.
        '''

        # call BaseException class constructor with the original error message
        super().__init__(error_message)

        # Generate detailed error message
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        '''
        Returns the detailed error message when the CustomExeption is raised.
        '''
        return self.error_message