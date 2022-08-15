from image_to_ascii import ImageToAscii
import argparse
import sys

class Dummy:
    img = False

class Dumbpassr:
    def print_help():
        sys.exit("usage: project.py [-h] [--img IMG] [--res {LOW,MEDIUM,HIGH}]")

def main():
    #Calling the Parser and assigning it's return value to arugs variable
    arugs, parser = parsr()

    if not arugs:
        passed = arg_check(arugs)
    else:
        sys.exit('Incorrect Arguements')

    if passed:
        txt, booln = text(arugs.img)
        if booln:
            converter(arugs.res, arugs.img, txt)
        else:
            pass
    else:
        parser.print_help()

def parsr():
    if ('--img' in sys.argv):
        #Instantiates Arguement parser with a befitting desciption
        parser = argparse.ArgumentParser(description="Image to ASCII art converter")
        #Adds the --res arguement to the parser
        parser.add_argument("--img", type=str, help='path to the location of the jpg image file')
        parser.add_argument("--res", type=str, choices=['LOW', 'MEDIUM', 'HIGH'], default='MEDIUM', help='selecting resolution of the ASCII art. default=medium')
        #Assigns the arguement recieved to the args variable
        args = parser.parse_args()
        #Returns args
        return args, parser
    else:
        return Dummy, Dumbpassr

#A Function to check for errors in the arguements passed
def arg_check(ag):
    if not ag.img:
        return False
    elif ".jpg" not in ag.img:
        return False
    else:
        return True

#A Function to give the name for the text which will be exported
def text(i):
    if ".jpg" in i:
        tfile = i.replace(".jpg", ".txt")
    else:
        return None, False

    return tfile, True

#The Function whicih executes the action of converting Image to Ascii art
def converter(resi, img, txt):
    
    LOW = 65
    MEDIUM = 100
    HIGH = 165
    rdict = {
        'LOW':65,
        'MEDIUM':100,
        'HIGH':165,
    }
    rlist = ['LOW', 'MEDIUM', 'HIGH']

    
    
    print(img, resi, txt)
    for i in rlist:
        if resi == i:
            res = rdict[i]
            ImageToAscii(img, res, txt)
            print("\n\n")
            print(f"CREATED {txt} FROM {img} WITH {resi.lower()} RESOLUTION...")
            print("ASCII IMAGE CREATED SUCCESSFULL!!!")

if __name__ == '__main__':
    main()