import urllib.request
import os

def main():
	request_url = os.environ['url']
	print('Connecting to {!s}'.format(request_url))
	page = urllib.request.urlopen(request_url)
	print('Completed successfully')

if __name__ == '__main__':
	main()