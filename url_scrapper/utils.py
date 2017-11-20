import pdfx
import requests

def ext_type_is_valid(filename, extension):
	return filename.endswith(extension)
	



def extract_urls_from_pdf(file_url):
	''' load pdf file, scrap content and extract and return a list of valid urls '''
	urls  =  []
	pdf = pdfx.PDFx(file_url)
	references = pdf.get_references_as_dict()
	for url in references['url']:
		if any([url.startswith('http'), url.startswith('www')]):
			urls.append(url)
	return urls



def check_url_status(url):
	error_code_first_char = ['4','5']
	response =  requests.get(url)
	str_status_code = str(response.status_code)
	if str_status_code[0] in error_code_first_char:
		return False, response.status_code
	return True, response.status_code


