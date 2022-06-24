# pyTelepass
# Copyright 2022 Emanuele Parini
#
# Module for extract text in PDF readable
#
import pdfplumber


def extract(file_name, page):
    with pdfplumber.open(file_name) as pdff:

        # extract first page info
        extract_line = 0
        if page == 0:
            print("Tot. pages: " + str(len(pdff.pages)))
            npage = pdff.pages[0].extract_text()
            for line in npage.split('\n'):
                if extract_line == 1:
                    return line
                if "DATA FATTURA" in line:
                    extract_line = 1
                else:
                    extract_line = 0
            return pdff.pages[0].extract_text()

        # extract other page lines
        res = ""
        exclude = 1
        for page in pdff.pages:
            if exclude == 0:
                npage = page.crop((0, 0.15 * float(page.height), page.width, page.height)).extract_text()
                for line in npage.split('\n'):
                    if "PED" in line:
                        res = res + '\n' + line
                    elif "APPARATO" in line:
                        res = res + '\n' + line
                    elif "TARGA" in line:
                        res = res + '\n' + line

            else:
                exclude = 0

        return res
