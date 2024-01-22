the challenge says "this one isn't exactly caeser but it might be the key", this suggests that the encryption
is vigenere, it's the same as the caeser decryption, but instead of always shifting with the same value, we
shift with the corresponding letter of the key. if the key is "al", we shift the first letter of the encrypted
text with "a" and the second with "l" and the next with "a" and we keep reitirating.
We try the vigenere decryption with key = "caeser" as it is indicated in the challenge text, we get an incoherent flag
but we do get some words that are coherent. If we try with key = "Caesar", we get the full text decrypted.
