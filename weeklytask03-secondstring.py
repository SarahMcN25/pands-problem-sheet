# this program inputs a string 
# then outputs every second letter of that string in reverse order
# Using sentence: "The quick brown fox jumps over the lazy dog."

# author: Sarah McNelis

sentence = input("Please enter a sentence:")
print (sentence [::-2])

# note -2 outputs every second step backwards
# minus indiactes the backwards and 2 indicates every second one
# eg [::3] would output every third letter starting from position 0 (start) to the end of sentence
# [::-3] would output every third letter backwards 
