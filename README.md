# regressive-imagery-dictionary

A pip-installable conversion of John Wiseman's Regressive Imagery Dictionary library.

"The Regressive Imagery Dictionary (RID) is a coding scheme for text analysis
that is designed to measure 'primordial' and conceptual content. Primordial
thought is the kind of free-form, associative thinking involved in fantasy
and dreams. Like Freud's id, I guess. Conceptual (or secondary) thought is
logical, reality-based and focused on problem solving."

via: [John Wiseman](http://lemonodor.com/archives/001511.html)

## Usage

To install:

```bash
$ pip install regressive-imagery-dictionary
```

To use:

```bash
$ cat README.md | rid

SECONDARY:ABSTRACTION                                           47
    scheme analysis conceptual thought thinking guess conceptual thought logical reality problem abstraction scheme analysis conceptual thought thinking guess conceptual thought logical reality problem abstraction scheme analysis conceptual thought thinking guess conceptual thought logical reality problem abstraction scheme analysis conceptual thought thinking guess conceptual thought logical reality problem
PRIMARY:SENSATION:VISION                                        25
    imagery imagery imagery imagery vision imagery imagery imagery imagery vision imagery imagery imagery imagery vision imagery imagery imagery imagery imagery imagery imagery imagery imagery imagery
EMOTIONS:AFFECTION                                              14
    kind like affection kind like affection kind like affection kind like affect affect affect
SECONDARY:ORDER                                                 11
    measure form order measure form order measure form order measure form
PRIMARY:NEED:ORALITY                                            11
    lemonodor orality lemonodor orality lemonodor orality lemonodor lemonodor lemonodor lemonodor lemonodor
PRIMARY:REGRESSIVE COGNITION:CONSCIOUSNESS ALTERATION            8
    fantasy dreams fantasy dreams fantasy dreams fantasy dreams
PRIMARY:SENSATION:GENERAL-SENSATION                              7
    sensation sensation sensation sensation sensation sensation sensation
SECONDARY:SOCIAL BEHAVIOR                                        7
    conversion social conversion social conversion social conversion
SECONDARY:INSTRUMENTAL BEHAVIOR                                  6
    use use use use copy copy
EMOTIONS:POSITIVE AFFECT                                         4
    enjoymentland enjoymentland enjoymentland enjoymentland

PRIMARY             : 36.428571 %
EMOTIONS            : 12.857143 %
SECONDARY           : 50.714286 %

245 words total
```

## References and inspiration:

- http://lemonodor.com/archives/001511.html
- http://enjoymentland.com/2010/01/11/the-regressive-imagery-dictionary/
