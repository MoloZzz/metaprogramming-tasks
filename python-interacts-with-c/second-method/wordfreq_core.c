#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "wordfreq_core.h"

// Helper function to convert string to lowercase
void to_lowercase(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

// Main function to find N most frequent words
WordFreq* find_frequent_words(const char* text, int n, int* result_size) {
    // Create a dynamic array for word frequencies
    WordFreq* freqs = NULL;
    int capacity = 0;
    int size = 0;

    // Copy text to modify
    char* text_copy = _strdup(text);
    if (!text_copy) return NULL;

    // Tokenize text
    char* token = strtok_s(text_copy, " \n\t.,!?;:'\"()[]{}", &text_copy);
    while (token) {
        // Convert to lowercase
        to_lowercase(token);

        // Skip empty tokens
        if (strlen(token) == 0) {
            token = strtok_s(NULL, " \n\t.,!?;:'\"()[]{}", &text_copy);
            continue;
        }

        // Check if word exists
        int found = 0;
        for (int i = 0; i < size; i++) {
            if (strcmp(freqs[i].word, token) == 0) {
                freqs[i].count++;
                found = 1;
                break;
            }
        }

        // Add new word if not found
        if (!found) {
            if (size >= capacity) {
                capacity = capacity == 0 ? 4 : capacity * 2;
                freqs = realloc(freqs, capacity * sizeof(WordFreq));
                if (!freqs) {
                    free(text_copy);
                    return NULL;
                }
            }
            freqs[size].word = _strdup(token);
            freqs[size].count = 1;
            size++;
        }

        token = strtok_s(NULL, " \n\t.,!?;:'\"()[]{}", &text_copy);
    }

    // Sort by frequency (descending) and word (ascending)
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (freqs[i].count < freqs[j].count ||
                (freqs[i].count == freqs[j].count && strcmp(freqs[i].word, freqs[j].word) > 0)) {
                WordFreq temp = freqs[i];
                freqs[i] = freqs[j];
                freqs[j] = temp;
            }
        }
    }

    // Limit to N results
    *result_size = (size < n) ? size : n;
    free(text_copy);
    return freqs;
}

// Free allocated memory
void free_wordfreq(WordFreq* freqs, int size) {
    for (int i = 0; i < size; i++) {
        free(freqs[i].word);
    }
    free(freqs);
}