
#sample DGA based off of code at https://en.wikipedia.org/wiki/Domain_generation_algorithm

def generate_domain(year: int, month: int, day: int) -> str:
    """Generate a domain name for the given date."""
    domain = ""

    for i in range(16):
    	# ^  = XOR
    	# >> = shift bits to the right eg 12 << 2 | 1100 (8+4) becomes 11 0000 (32+16)
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        #eg. 8 * 2020 = 2020 ^ 16160 = 0011111100100000 ^ 0000011111100100 = 14532
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    return domain + ".com"

if __name__ == '__main__':
	from datetime import datetime as d
	print(generate_domain(d.now().year,d.now().month,d.now().day))

    #import re
    #date = str(d.now())
    #date_re = re.findall('\d*',date)
    #print(generate_domain(int(date_re.pop(0)),int(date_re.pop(1)),int(date_re.pop(2))))