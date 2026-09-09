input_write=open("input.txt","w")
input_write.write("This is a test file for input and output operations.\n")
input_write.write("We will write some data to this file and then read it back.\n")
input_write.close()
input_read=open("input.txt","r")
input_data=input_read.read()
input_read.close()
words=input_data.split()
word_counts={}
for word in words:
    word=word.lower()
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word]=1
output_write=open("output.txt","w")
for word,count in word_counts.items():
    output_write.write(f"{word}: {count}\n")
output_write.close()