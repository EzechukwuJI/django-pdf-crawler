Assumptions And observations:

** visit pypdfcrawler.herokuapp.com/upload to get started

1. A TemporaryFile model class is required to hold the uploaded file in order 
to expose the url attribute of the file(pdf) object which is required by pdfx for parsing. Also, we cannot rely completely on user uploaded document and that calls for a little caution when dealing with uploaded files.

2. There is a huge delay in the scrapping time, I guess this is because the system makes a GET request to each retrieved URL using requests, to check if the url is live or not. I am still experimenting on how to cut down this delay. 
