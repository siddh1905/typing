import time
import random
import msvcrt
from colorama import init, Fore, Style

init()

sentences = [
    "Practice makes perfect typing skills",
    "Python is a great language to learn",
    "Typing fast helps save precious time",
    "Errors should be corrected early",
    "Focus on accuracy over speed",
    "The quick brown fox jumps over the lazy dog",
    "Consistent effort leads to better performance",
    "Coding requires patience and problem solving",
    "Typing is an essential computer skill today",
    "Always review your work before submitting",
    "Small improvements daily lead to big success",
    "Keyboard mastery boosts productivity greatly",
    "Use proper posture while typing for comfort",
    "Avoid looking at the keyboard when typing",
    "Muscle memory helps you type without thinking",
    "Typing tests are good for building confidence",
    "Set daily goals to improve your typing speed",
    "Stay relaxed and focused while practicing",
    "Challenge yourself with harder typing drills",
    "Measure both speed and accuracy for progress"
]

def get_char():
    return msvcrt.getwch()

def print_feedback(target, typed):
    display = ""
    for i in range(len(target)):
        if i < len(typed):
            if typed[i] == target[i]:
                display += Fore.GREEN + typed[i]
            else:
                display += Fore.RED + typed[i]
        else:
            display += Fore.LIGHTBLACK_EX + target[i]
    display += Style.RESET_ALL
    print("\r" + display + " " * (len(target) - len(typed)), end='', flush=True)

def typing_test():
    sentence = random.choice(sentences)
    print("\n--- Typing Speed Test ---")
    print("\nType the following sentence:\n")
    print(Fore.LIGHTBLACK_EX + sentence + Style.RESET_ALL)
    print("\nStart typing below. Your input will be shown live with color-coded feedback.\n")

    words = sentence.split()
    typed_words = []
    current_word = ''
    all_typed = ''
    started = False

    while True:
        char = get_char()

        if not started:
            start_time = time.time()
            started = True

        if char == '\r':
            if current_word:
                typed_words.append(current_word)
            break

        elif char == ' ':
            if current_word:
                typed_words.append(current_word)
                all_typed += current_word + ' '
                current_word = ''
            print_feedback(sentence, all_typed)
        elif char == '\b':
            if len(current_word) > 0:
                current_word = current_word[:-1]
                all_typed = all_typed[:-1]
            print_feedback(sentence, all_typed + current_word)
        else:
            current_word += char
            all_typed += char
            print_feedback(sentence, all_typed)

    end_time = time.time()
    time_taken = end_time - start_time
    wpm = (len(typed_words) / time_taken) * 60
    correct = 0

    print("\n\n--- Results ---")
    for i in range(len(words)):
        if i < len(typed_words) and typed_words[i] == words[i]:
            correct += 1
            print(Fore.GREEN + f"[✓] {typed_words[i]}" + Style.RESET_ALL)
        elif i < len(typed_words):
            print(Fore.RED + f"[✗] {typed_words[i]} (Expected: {words[i]})" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[✗] (Missing word: {words[i]})" + Style.RESET_ALL)

    accuracy = (correct / len(words)) * 100
    print(f"\nTime Taken       : {round(time_taken, 2)} seconds")
    print(f"Typing Speed     : {round(wpm, 2)} WPM")
    print(f"Accuracy         : {round(accuracy, 2)}%")

if __name__ == "__main__":
    typing_test()
