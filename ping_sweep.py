#!/usr/bin/python3
def main():
    from os import system
    strip_char = '.'
    range_sweep = input('enter ip range to scan here (eg. 192.168.1.0-255): ')
    ping_range_end = range_sweep.split('-')[-1]
    ping_range_start = range_sweep.split('-')[0]
    lol = ping_range_start.find('.')
    lol = ping_range_start.find('.', lol + 2)
    lol = ping_range_start.find('.', lol + 2)
    lol = ping_range_start[lol+1]
    ping_range_start = strip_char.join(ping_range_start.split(strip_char)[:3])
    for i in range(int(lol),int(ping_range_end)+1):
        system('ping -c 4 ' + ping_range_start + '.' + str(i))

if __name__ == '__main__':
    main()
