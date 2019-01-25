from bs4 import BeautifulSoup
import urllib.request as ur


def main():
    target = "http://rosalind.info/problems/tree-view/"
    r = ur.urlopen(target).read()
    soup  = BeautifulSoup(r, "lxml")

    problems = soup.find_all("g", attrs={"class": "node"})

    with open('problems_dump.txt', 'w') as f:
    	f.write(str(problems))
    f.close()

if __name__ == '__main__':
	main()

