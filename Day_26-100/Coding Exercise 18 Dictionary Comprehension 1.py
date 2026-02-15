sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word_key:len(word_key) for word_key in sentence.split()}
print(result)