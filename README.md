# The /// Interpreter

This is a simple Python interpreter for the /// programming language
written by Carlos Luna Mota (https://github.com/CarlosLunaMota/Slashes).


## Input

The interpreter function `slashes(string, verbose=0)` requires an input
string (`string`) with the executable code and accepts an optional integer
parameter (`verbose`) that controls the verbosity of the interpreter:

* If `verbose == 0` no debug information is printed.
* If `verbose >= 1` prints the initial input and the final output.
* If `verbose >= 2` prints the main substitution steps.
* If `verbose >= 3` prints all the substitution steps.
* If `verbose >= 4` stops at the main substitution steps.
* If `verbose >= 5` stops at every substitution step.

Since Python uses `\` as escape character, you might need to either use raw
strings or duplicate all the backslashes of the input string (e.g. these
two codes are equivalent):

    program_1 = r"/foo/Hello, world!//B\/\\R/foo/B/\R"
    program_2 = "/foo/Hello, world!//B\\/\\\\R/foo/B/\\R"


## Output

The interpreter returns a generator function that yields the output one
character at a time. You can use:

    output = "".join(slashes(code_to_execute))

to obtain the whole output as a single string.


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 


# The /// esoteric programming language

/// (pronounced "slashes") is a minimalist Turing-complete esoteric
programming language, invented by Tanner Swett in 2006.

You can find more information about /// at: <https://esolangs.org/wiki////>


## Language Especification

> *Language especification taken from: <https://esolangs.org/wiki////>*

If the program is empty, execution halts. Otherwise, the first character is
taken, and execution proceeds as follows:

* If the character is `\`, the character after it (if any) is printed and
  both characters are removed from the program.
* If the character is `/`, it is removed, the pattern and replacement are
  identified and a substitution is performed.
* Otherwise, the character is printed and removed.

The execution process then starts over again with the modified program.


### Pattern

A substitution starts by reading characters in a loop to make up the
pattern, as follows:

* If the character read is `\`, the character after it is added to the
  pattern, and both characters are removed.
* If the character read is `/`, it is removed, and the pattern-reading
  process ends.
* Otherwise, the character is added to the pattern and removed.

If this process reaches the end of the program without reaching a
terminating `/`, then the program halts.


### Replacement

Otherwise, the same process is repeated again, making up the replacement.

* If the character read is `\`, the character after it is added to the
  replacement, and both characters are removed.
* If the character read is `/`, it is removed, and the replacement-reading
  process ends.
* Otherwise, the character is added to the replacement and removed.

Again, if no terminating `/` is reached, the program halts.


### Substitution

Now that the pattern and replacement have both been read, the substitution
process begins.

If the pattern is empty, then the program loops forever (which is the
mathematically obvious result of replacing all occurrences of the empty
string). If there are no occurrences of the pattern in the rest of the
program, then the substitution ends. Otherwise, the first occurrence in
the text is replaced by the replacement, and the substitution repeats.

Note that a replacement which contains the pattern will cause an infinite
loop; for example, `/foo/foobar/foo` will evolve as follows:

    /foo/foobar/foo
    /foo/foobar/foobar
    /foo/foobar/foobarbar
    /foo/foobar/foobarbarbar
    ...

As the substitution process never ends, the program never halts, and
nothing is printed.

Such an infinite loop is possible even without a replacement containing
the pattern, e.g. `/ab/bbaa/abb`:

    /ab/bbaa/abb
    /ab/bbaa/bbaab
    /ab/bbaa/bbabbaa
    /ab/bbaa/bbbbaabaa
    /ab/bbaa/bbbbabbaaaa
    ...


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 


# LICENSE

This file was created by Carlos Luna Mota and is released into de public
domain using the following license:

> This is free and unencumbered software released into the public domain.
>
> Anyone is free to copy, modify, publish, use, compile, sell, or
> distribute this software, either in source code form or as a compiled
> binary, for any purpose, commercial or non-commercial, and by any
> means.
> 
> In jurisdictions that recognize copyright laws, the author or authors
> of this software dedicate any and all copyright interest in the
> software to the public domain. We make this dedication for the benefit
> of the public at large and to the detriment of our heirs and
> successors. We intend this dedication to be an overt act of
> relinquishment in perpetuity of all present and future rights to this
> software under copyright law.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
> IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
> OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
> ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
> OTHER DEALINGS IN THE SOFTWARE.
> 
> For more information, please refer to <http://unlicense.org>
