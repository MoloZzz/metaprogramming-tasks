#ifndef WORDFREQ_CORE_H
#define WORDFREQ_CORE_H

typedef struct {
    char* word;
    int count;
} WordFreq;

void to_lowercase(char* str);
WordFreq* find_frequent_words(const char* text, int n, int* result_size);
void free_wordfreq(WordFreq* freqs, int size);

#endif /* WORDFREQ_CORE_H */