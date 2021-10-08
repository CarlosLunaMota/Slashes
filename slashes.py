#!/usr/bin/env python

### Python 2/3 compatibility hack ###
try: input = raw_input              #
except NameError: pass              #
#####################################



### INTRODUCTION ###############################################################
#
#   # The /// Interpreter
#
#   This is a simple Python interpreter for the /// programming language
#   written by Carlos Luna Mota (https://github.com/CarlosLunaMota/Slashes).
#
#
#   ## Input
#
#   The interpreter function `slashes(string, verbose=0, color=0)` requires an
#   input string (`string`) with the executable code and accepts two optional
#   integer parameters (`verbose` and `color`) that control the interpreter's
#   output:
#
#   * If `verbose <= 0` no debug information is printed (default).
#   * If `verbose >= 1` prints the initial input and the final output.
#   * If `verbose >= 2` prints the main substitution steps.
#   * If `verbose >= 3` prints all the substitution steps.
#   * If `verbose >= 4` stops at the main substitution steps.
#   * If `verbose >= 5` stops at every substitution step.
#
#   * If `color <= 0` no color highlighting is applied to the output (default).
#   * If `color == 1` subtle grayscale highlighting is applied to the output.
#   * If `color >= 2` bright color highlighting is applied to the output.
#
#   Since Python uses `\` as escape character, you might need to either use raw
#   strings or duplicate all the backslashes of the input string (e.g. these
#   two codes are equivalent):
#
#       program_1 = r"/foo/Hello, world!//B\/\\R/foo/B/\R"
#       program_2 = "/foo/Hello, world!//B\\/\\\\R/foo/B/\\R"
#
#
#   ## Output
#
#   The interpreter returns a generator function that yields the output one
#   character at a time. You can use:
#
#       output = "".join(slashes(code_to_execute))
#
#   to obtain the whole output as a single string.
#
#
#   ---------------------------------------------------------------------------
#
#
#   # The /// esoteric programming language
#
#   /// (pronounced "slashes") is a minimalist Turing-complete esoteric
#   programming language, invented by Tanner Swett in 2006.
#
#   You can find more information about /// at: <https://esolangs.org/wiki////>
#
#
#   ## Language Especification
#
#   > *Language especification taken from: <https://esolangs.org/wiki////>*
#
#   If the program is empty, execution halts. Otherwise, the first character is
#   taken, and execution proceeds as follows:
#
#   * If the character is `\`, the character after it (if any) is printed and
#     both characters are removed from the program.
#   * If the character is `/`, it is removed, the pattern and replacement are
#     identified and a substitution is performed.
#   * Otherwise, the character is printed and removed.
#
#   The execution process then starts over again with the modified program.
#
#
#   ### Pattern
#
#   A substitution starts by reading characters in a loop to make up the
#   pattern, as follows:
#
#   * If the character read is `\`, the character after it is added to the
#     pattern, and both characters are removed.
#   * If the character read is `/`, it is removed, and the pattern-reading
#     process ends.
#   * Otherwise, the character is added to the pattern and removed.
#
#   If this process reaches the end of the program without reaching a
#   terminating `/`, then the program halts.
#
#
#   ### Replacement
#
#   Otherwise, the same process is repeated again, making up the replacement.
#
#   * If the character read is `\`, the character after it is added to the
#     replacement, and both characters are removed.
#   * If the character read is `/`, it is removed, and the replacement-reading
#     process ends.
#   * Otherwise, the character is added to the replacement and removed.
#
#   Again, if no terminating `/` is reached, the program halts.
#
#
#   ### Substitution
#
#   Now that the pattern and replacement have both been read, the substitution
#   process begins.
#
#   If the pattern is empty, then the program loops forever (which is the
#   mathematically obvious result of replacing all occurrences of the empty
#   string). If there are no occurrences of the pattern in the rest of the
#   program, then the substitution ends. Otherwise, the first occurrence in
#   the text is replaced by the replacement, and the substitution repeats.
#
#   Note that a replacement which contains the pattern will cause an infinite
#   loop; for example, `/foo/foobar/foo` will evolve as follows:
#
#       /foo/foobar/foo
#       /foo/foobar/foobar
#       /foo/foobar/foobarbar
#       /foo/foobar/foobarbarbar
#       ...
#
#   As the substitution process never ends, the program never halts, and
#   nothing is printed.
#
#   Such an infinite loop is possible even without a replacement containing
#   the pattern, e.g. `/ab/bbaa/abb`:
#
#       /ab/bbaa/abb
#       /ab/bbaa/bbaab
#       /ab/bbaa/bbabbaa
#       /ab/bbaa/bbbbaabaa
#       /ab/bbaa/bbbbabbaaaa
#       ...
#   
#
#   ---------------------------------------------------------------------------
#
#
#   # LICENSE
#
#   This file was created by Carlos Luna Mota and is released into de public
#   domain using the following license:
#
#   > This is free and unencumbered software released into the public domain.
#   >
#   > Anyone is free to copy, modify, publish, use, compile, sell, or
#   > distribute this software, either in source code form or as a compiled
#   > binary, for any purpose, commercial or non-commercial, and by any
#   > means.
#   > 
#   > In jurisdictions that recognize copyright laws, the author or authors
#   > of this software dedicate any and all copyright interest in the
#   > software to the public domain. We make this dedication for the benefit
#   > of the public at large and to the detriment of our heirs and
#   > successors. We intend this dedication to be an overt act of
#   > relinquishment in perpetuity of all present and future rights to this
#   > software under copyright law.
#   > 
#   > THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#   > EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#   > MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#   > IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#   > OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#   > ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#   > OTHER DEALINGS IN THE SOFTWARE.
#   > 
#   > For more information, please refer to <http://unlicense.org>
#
################################################################################

import sys


### /// INTERPRETER ############################################################

def slashes(string, verbose=0, color=0):

    # Print Debug Info and Set Color Scheme #########################
    if verbose >  0: output = []; print("INPUT:  " + string + "\n") #
    if   color <= 0: X = ["/", "/", "/", "\n"]                      #
    elif color == 1: X = ["\033[0;1m/\033[0;2m"]*3 + ["\033[0m\n"]  #
    elif color >= 2: X = ["\033[0;2;90m/\033[0;91m",                #
                          "\033[0;2;90m/\033[0;92m",                #
                          "\033[0;2;90m/\033[0;96m", "\033[0m\n"]   #        
    #################################################################

    while string:

        N = len(string)

        # Output whatever appears before the fist unescaped "/":
        i = 0
        while i < N:
            if string[i] == "/" : break
            if string[i] == "\\": i += 1

            ### Store Debug Info #####################
            if verbose > 0: output.append(string[i]) #
            ##########################################
            
            yield string[i]
            i += 1

        # Find the Pattern betwen the fist and the second unescaped "/":
        i, pattern = i+1, []
        while i < N:
            if string[i] == "/" : break
            if string[i] == "\\": i += 1
            pattern.append(string[i])
            i += 1

        # Find the Replacement betwen the second and the third unescaped "/":
        i, replacement  = i+1, []
        while i < N:
            if string[i] == "/" : break
            if string[i] == "\\": i += 1
            replacement.append(string[i])
            i += 1

        # If there are less than three unescaped "/": halt
        if i >= N: break

        # Otherwise: perform as many Substitutions as possible
        pat    = "".join(pattern)
        rep    = "".join(replacement)
        string = string[i+1:]

        # Print Debug Info ##########################################
        if verbose > 1:                                             #
            print("APPLY:  "+X[0]+pat+X[1]+rep+X[2]+string+X[3])    #
            if verbose > 3:                                         #
                _ = input("\nPress <Return> to resume execution")   #
                print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")        #
        #############################################################

        while pat in string:
            string = string.replace(pat, rep, 1)

            # Print Debug Info ##########################################
            if verbose > 2:                                             #
                print("APPLY:  "+X[0]+pat+X[1]+rep+X[2]+string+X[3])    #
                if verbose > 4:                                         #
                    _ = input("\nPress <Return> to resume execution")   #
                    print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")        #
            #############################################################

    # Print Debug Info ##################################
    if verbose > 0: print("OUTPUT: " + "".join(output)) #
    #####################################################

################################################################################



### COMPACT /// INTERPRETER ####################################################

def S(s):
  while s:
    b = ["","",1]
    for t in (0,1,2):
      while s:
        if s[0] == "/" :      s = s[1:]; break
        if s[0] == "\\":      s = s[1:]
        if t: b[t-1] += s[0]; s = s[1:]
        else: yield     s[0]; s = s[1:]
    while s and b[0] in s: s = s.replace(*b)

################################################################################



### MAIN #######################################################################

if __name__ == "__main__":

    # Some sample programs:
    
    HELLO_WORLD_0 = "Hello, world!"
    HELLO_WORLD_1 = "/ world! world!/Hello,/ world! world! world!"
    HELLO_WORLD_2 = "/foo/Hello, world!//bar/foo/bar"
    HELLO_WORLD_3 = "Hello, /foo/bar/World/asdf/qwer/!"
    HELLO_WORLD_4 = "/-/World//--/Hello//--W/--, w/---!"
    HELLO_WORLD_5 = r"/foo/Hello, world!//B\/\\R/foo/B/\R"
    HELLO_WORLD_6 = "/foo/Hello, world!//B\\/\\\\R/foo/B/\\R"

    THUE_MORSE = r"""/
        //
        />*/#>/
        />/\/.\/\/.0/
        /#/\/.\\0\/,\\,0,\\,1\/\/.\\1\/,\\,1,\\,0\/\/,\\,\/.\//
        >
        """
        
    FIBONACCI = r"""/
        //
        />*/#>/
        />/\/.\/\/\/+\\+\/\/\/-\/\\\\\\\/\/\/0\/1\/\/1\/*\/++.1/
        /#/\/.\\0\/,\\,0,\\,1\/\/.\\1\/,\\,0\/\/,\\,\/.\/\/+\\+\/=\\=.\\1-\/\/=\\=\/+\\+\//
        >
        """
        
    UNARY_TO_ROMAN = r"""/
        //
        /*/I/
        /IIIII/V/
        /IIII/IV/
        /VV/X/
        /VIV/IX/
        /XXXXX/L/
        /XXXX/XL/
        /LL/C/
        /LXL/XC/
        /CCCCC/D/
        /CCCC/CD/
        /DD/M/
        /DCD/CM/
        """

    ROMAN_TO_UNARY = r"""/
        //
        /CM/DCD/
        /M/DD/
        /CD/CCCC/
        /D/CCCCC/
        /XC/LXL/
        /C/LL/
        /XL/XXXX/
        /L/XXXXX/
        /IX/VIV/
        /X/VV/
        /IV/IIII/
        /V/IIIII/
        /I/*/
        """

    DECIMAL_TO_UNARY = r"""/
        //
        /9/8*/
        /8/7*/
        /7/6*/
        /6/5*/
        /5/4*/
        /4/3*/
        /3/2*/
        /2/1*/
        /1/0*/
        /*0/9*/
        /0//
        """

    UNARY_TO_DECIMAL = r"""/
        //
        /*/>01/
        /1>/1/
        /10/01/
        /01111111111/1\0/
        /0111111111/_9/
        /011111111/_8/
        /01111111/_7/
        /0111111/_6/
        /011111/_5/
        /01111/_4/
        /0111/_3/
        /011/_2/
        /01/_1/
        /_//
        />0/>/
        />//
        """

    BINARY_TO_UNARY = r"""/
        //
        /1/0*/
        /*0/0**/
        /0//
        """
    
    UNARY_TO_BINARY = r"""/
        //
        /*/>01/
        /1>/1/
        /10/01/
        /011/1\0/
        /01/_1/
        /_//
        />0/>/
        />//
        """

    BINARY_SUMS = r"""/
        //
        / //
        /++/+/
        /-+/+/
        /+-/-/
        /--/-/
        /11/0*0*/
        /10/0*0/
        /01/00*/
        /*0/0**/
        /0*/*/
        /+0//
        /-0//
        /+1/+*/
        /-1/-*/
        /-*/#-/
        /#-/#/
        /+//
        /1#//
        /1*/**/
        /0#/#/
        /0\*/*/
        /*#//
        /#*//
        /#/-OI/
        /I-/I/
        /*/>OI/
        /I>/I/
        /IO/OI/
        /OII/I\O/
        /OI/_I/
        /_//
        /-O/-/
        />O/>/
        />//
        /I/1/
        /O/0/
        """

    # Run them all:

    _ = "".join(slashes(HELLO_WORLD_0, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_1, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_2, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_3, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_4, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_5, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(HELLO_WORLD_6, verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(THUE_MORSE+"*****", verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(FIBONACCI+"*********", verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(DECIMAL_TO_UNARY+"34", verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(UNARY_TO_DECIMAL+"**********************************",
                        verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(BINARY_TO_UNARY+"100010", verbose=3, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(UNARY_TO_BINARY+"**********************************",
                        verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(ROMAN_TO_UNARY+"XXXIV", verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(UNARY_TO_ROMAN+"**********************************",
                        verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

    _ = "".join(slashes(BINARY_SUMS+" 1-1+0-10000+101++1+0-1---0 +  10 11- 1 0",
                        verbose=1, color=2))

    print("\n--------------------------------------------------------------\n")

################################################################################

if __name__ == "__main__":
    with open(sys.argv[1],"r") as handle:
        slashes(handle.read())