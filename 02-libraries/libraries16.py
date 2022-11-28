import os

from tqdm import tqdm


def main():
    size = os.path.getsize('libraries16.py')
    with tqdm(total=size) as pbar:
        with open('libraries16.py', 'r') as f:
            for line in f:
                pbar.update(len(line))
                if 'python' in line.lower():
                    print(line)
                    break


if __name__ == '__main__':
    main()
