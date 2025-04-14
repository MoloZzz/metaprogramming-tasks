# distutils: language = c
# distutils: sources = wordfreq_core.c
# cython: language_level=3

cdef extern from "wordfreq_core.h":
    ctypedef struct WordFreq:
        char* word
        int count

    WordFreq* find_frequent_words(const char* text, int n, int* result_size)
    void free_wordfreq(WordFreq* freqs, int size)

def get_frequent_words(str text, int n):
    """
    Find the N most frequent words in the text.
    Returns a dictionary with words and their counts.
    """
    # Convert Python string to bytes and keep it alive
    cdef bytes py_bytes = text.encode('utf-8')
    cdef const char* c_text = py_bytes

    cdef int result_size
    cdef WordFreq* result = find_frequent_words(c_text, n, &result_size)

    if result == NULL:
        raise MemoryError("Failed to process text")

    # Convert C results to Python dictionary
    word_dict = {}
    for i in range(result_size):
        word = result[i].word.decode('utf-8')
        count = result[i].count
        word_dict[word] = count

    # Free memory
    free_wordfreq(result, result_size)
    return word_dict