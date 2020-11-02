##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import argparse
from time import time
import os

from fnc.extractFeature import extractFeature
from fnc.matching import matching

#------------------------------------------------------------------------------
#	Argument parsing
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str, default="./../CASIA1/1/001_2_4.jpg" ,
					help="Path to the file that you want to verify.")

parser.add_argument("--temp_dir", type=str, default="./templates/",
					help="Path to the directory containing templates.")

parser.add_argument("--thres", type=float, default=0.38,
					help="Threshold for matching.")

args = parser.parse_args()

def main():		
	##-----------------------------------------------------------------------------
	##  Execution
	##-----------------------------------------------------------------------------
	# Extract feature
	start = time()
	print('>>> Start verifying {}\n'.format(args.file))

	if not os.path.exists(args.temp_dir):
        	os.makedirs(args.temp_dir)

	template, mask, file = extractFeature(args.file)


	# Matching
	result = matching(template, mask, args.temp_dir, args.thres)
	print('result = ' , result)

	if result == -1:
		print('>>> No registered sample.')

	elif result == 0:
		print('>>> No sample matched.')

	else:
		print('>>> {} samples matched (descending reliability):'.format(len(result)))
		for res in result:
			print("\t", res)

		print("user "+result[0][1:3]+" identified successfully.")


	# Time measure
	end = time()
	print('\n>>> Verification time: {} [s]\n'.format(end - start))


if __name__ == '__main__':
	main()