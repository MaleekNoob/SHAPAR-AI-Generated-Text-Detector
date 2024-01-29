import random


def read_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file]
    return sentences


def write_sentences(file_path, sentences):
    with open(file_path, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')


def main():
    train_file_path = 'gpt_data.txt'
    random_file_path = 'final_train.csv'

    # Read sentences from train_data.txt
    sentences = read_sentences(train_file_path)

    # Shuffle the sentences randomly
    random.shuffle(sentences)

    # Write shuffled sentences to random_data.txt
    write_sentences(random_file_path, sentences)

    print(f"Data shuffled and saved to {random_file_path}")


if __name__ == "__main__":
    main()
