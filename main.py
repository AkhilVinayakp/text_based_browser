nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
import argparse as arg
import os

parser = arg.ArgumentParser()
parser.add_argument('dir', help='directory name')
args = parser.parse_args()
if not os.path.exists(args.dir):
    os.mkdir(args.dir)


def save_file(filename, content):
    filename = filename.rsplit('.', maxsplit=1)[0]
    with open(os.path.join(args.dir, filename + '.txt'), 'w') as f:
        f.write(content)


ln = True
while ln:
    url = input('> ')
    if url == 'exit':
        ln = False
        continue
    file_name = url.rsplit('.', maxsplit=1)[0]+'.txt'
    for i in url:
        lc = list(filter(lambda x: x == '.', url))
    if any(lc):
        if url == "bloomberg.com":
            print(bloomberg_com)
            save_file(url, bloomberg_com)
        elif url == 'nytimes.com':
            print(nytimes_com)
            save_file(url, nytimes_com)
        else:
            print('Error: Incorrect URL')

    elif os.path.exists(os.path.join(args.dir, file_name)):
        with open(os.path.join(args.dir, file_name), 'r') as f:
            print(f.read())
    else:
        print('Error: Incorrect URL')