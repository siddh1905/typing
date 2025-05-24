import time

def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time  
    words = typed_text.split()
    num_words = len(words)
    wpm = (num_words / time_taken) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def typing_test():
    sample_text = "The quick brown fox jumps over the lazy dog."
    print("Typing Speed Test")
    print("Type the following sentence:\n")
    print(sample_text)
    input("\nPress Enter when you are ready...")

    start_time = time.time()
    typed_text = input("\nStart Typing: ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(sample_text, typed_text)

    print("\n--- Results ---")
    print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
    print(f"Words Per Minute (WPM): {wpm}")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_test()
