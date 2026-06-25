import tiktoken 

enc = tiktoken.encoding_for_model("gpt-4")

text = "Hey there ! my name is Ayan shaikh"
tokens = enc.encode(text)

# this is the output token of the given text "[1837, 86, 1070, 758, 856, 836, 374, 362, 8503, 16249, 31603]"
print(tokens)

print(enc.decode([1837, 86, 1070, 758, 856, 836, 374, 362, 8503, 16249, 31603]))  
