# pyTelepass
# Copyright 2022 Emanuele Parini
#
# Module for extract text from Telepass Invoice
#
import glob
import os
import module.pdf_text as pdftext

extract_line = 0

# Loop file to work
for filename in glob.iglob('file/*.pdf'):
    print(filename)

    # return header
    header = pdftext.extract(filename, 0)
    print(header)

    # return pages
    pages = pdftext.extract(filename, 1)
    print(pages)
