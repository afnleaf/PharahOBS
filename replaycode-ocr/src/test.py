import ocr
import cv2 as cv

'''
image_case1.png
SJZ8S6
RB3DWQ
W6TVD4

image_case2.png
5QRXK8
K5S5VX
RBDCJX
BS20AY
X98G8W
9F4836

image_case3.png
Y38XS1
R952V4
J93BN0

image_case4.png
80HYE7
NPM5JX

image_case5.png
8V0MSY
1QJAMX
JD02QC
8REZZV
5R2SD7
P1MJN8

image_case6.png
62Q07Z
9H99FR
G1MBST
A8ZHRV
S64RWC
P9NAVK

image_case7.png
TM6E6R
J8VQRY
NQSJMR
3V6MHE
9SX7TQ
BYGC49

image_case8.png
SDMB01
Q21EWS
60J3WT
C8CW12
WFQXQ0
GXRY73

image_case9.png
M2EBK2
XAGB46
BN8GYB
AKW0JE
S1SWZ9

image_case10.png
358XNX
4ST3DV
JFN24S
M09EWV
WW502Q
FR5TEM
EEEEBT

image_case11.png
358XNX
4ST3DV
JFN24S
M09EWV
WW502Q
FR5TEM
EEEEBT

image_case12.png
JX0PPY
6T4Z0G
BS967Q
QR2GE9
6NMKMW
1DHW1G

image_case13.png
HCEE2G
0QVMAR
203Y28
7AZT8Z
BKAXGN

image_case14.png
KYCWC7
J6X7J4
BHCJJ7
9HK8ZS
8MKTKC
C2M5FM

image_case15.png
948X72
A7W84R
RV1HFT
W865GQ
4GXQ98
BXR2N5
8RTN42
'''





def load_test_cases():
    test_cases = {
        "image_case1.png": ["SJZ8S6", "RB3DWQ", "W6TVD4"],
        "image_case2.png": ["5QRXK8", "K5S5VX", "RBDCJX", "BS20AY", "X98G8W", "9F4836"],
        "image_case3.png": ["Y38XS1", "R952V4", "J93BN0"],
        "image_case4.png": ["80HYE7", "NPM5JX"],
        "image_case5.png": ["8V0MSY", "1QJAMX", "JD02QC", "8REZZV", "5R2SD7", "P1MJN8"],
        "image_case6.png": ["62Q07Z", "9H99FR", "G1MBST", "A8ZHRV", "S64RWC", "P9NAVK"],
        "image_case7.png": ["TM6E6R", "J8VQRY", "NQSJMR", "3V6MHE", "9SX7TQ", "BYGC49"],
        "image_case8.png": ["SDMB01", "Q21EWS", "60J3WT", "C8CW12", "WFQXQ0", "GXRY73"],
        "image_case9.png": ["M2EBK2", "XAGB46", "BN8GYB", "AKW0JE", "S1SWZ9"],
        "image_case10.png": ["358XNX", "4ST3DV", "JFN24S", "M09EWV", "WW502Q", "FR5TEM", "EEEEBT"],
        "image_case11.png": ["358XNX", "4ST3DV", "JFN24S", "M09EWV", "WW502Q", "FR5TEM", "EEEEBT"],
        "image_case12.png": ["JX0PPY", "6T4Z0G", "BS967Q", "QR2GE9", "6NMKMW", "1DHW1G"],
        "image_case13.png": ["HCEE2G", "0QVMAR", "203Y28", "7AZT8Z", "BKAXGN"],
        "image_case14.png": ["KYCWC7", "J6X7J4", "BHCJJ7", "9HK8ZS", "8MKTKC", "C2M5FM"],
        "image_case15.png": ["948X72", "A7W84R", "RV1HFT", "W865GQ", "4GXQ98", "BXR2N5", "8RTN42"]
    }
    return test_cases

# main function, testing when bot is in prod
def main():
    template_filename="/app/images/template_large.png"
    template = ocr.load_template(template_filename)
    list_of_templates = ocr.create_templates(template)

    test_cases = load_test_cases()

    list_of_replaycodes = []
    input_append="/app/images/test_cases/"
    for i, case in enumerate(test_cases):
        print(case)
        #input_filename = input_append + f"image_case{i+1}.png"
        input_filename = input_append + case
        image = cv.imread(input_filename)
        assert image is not None, "File could not be read"
        crops = ocr.template_match(image, list_of_templates)
        replaycodes = ocr.process_codes(crops)
        list_of_replaycodes.append(replaycodes)

    print("\nTesting:")
    for i, replaycodes in enumerate(list_of_replaycodes):
        print(f"Case {i+1}")
        input_filename = f"image_case{i+1}.png"
        case_codes = test_cases[input_filename]
        passed = len(case_codes)
        for j, code in enumerate(replaycodes):
            _pass = "✅"
            if code != case_codes[j]:
                _pass = "❌"
                passed -= 1
            
            print(f"{j+1} -- output: {code}\treal: {case_codes[j]}\tpass: {_pass}")
        acc = passed / len(case_codes)
        print(f"Accuracy: {acc}")
        print()
        



# Default notation
if __name__ == "__main__":
    main()
