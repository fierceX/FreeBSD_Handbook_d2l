import os
import re
import sys

level = [
    'part',
    'chapter',
    'section',
    'subsection',
    'subsubsection',
    'subsubsubsection'
]


def main():
    tex_file = sys.argv[1]
    with open(tex_file, 'r') as f:
        lines = f.read().split('\n')
    
    for i,_ in enumerate(lines):
        if '\documentclass[' in lines[i]:
            lines[i] = '\documentclass[letterpaper,10pt,english,oneside]{sphinxmanual}'
        s = re.findall('\\\\(part)\{|\\\\(chapter)\{|\\\\(section)\{|\\\\(subsection)\{|\\\\(subsubsection)\{|\\\\(subsubsubsection)\{|\\\\(subsubsubsubsection)\{',lines[i])
        if s and '{FreeBSD 手册}' not in lines[i] and '{概述}' not in lines[i]:
            ss = set(s[0])
            ss.remove('')
            nl = list(ss)[0]
            lines[i] = lines[i].replace(nl,level[level.index(nl)-1])
        if 'sphinxlogo' in lines[i]:
            lines[i] = lines[i].replace('sphinxincludegraphics','includegraphics[width=0.4\linewidth]')

    with open(tex_file, 'w') as f:
        f.write('\n'.join(lines))


if __name__ == "__main__":
    main()