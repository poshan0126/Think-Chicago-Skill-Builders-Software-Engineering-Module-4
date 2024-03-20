import mood_response as mr

def main():
    mood = input("How are you feeling today? ")
    print(mr.mood_response(mood))

if __name__ == "__main__":
    main()
