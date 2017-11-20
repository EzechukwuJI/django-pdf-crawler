Assumptions Made:

** visit pypdfcrawler.herokuapp.com/upload to get started

1. A TemporaryFile model class is required to hold the uploaded file in order 
to expose the url attribute of the file(pdf) object which is required by pdfx for parsing. Also, we cannot rely completely on user uploaded document and that calls for a little caution when dealing with uploaded files.


