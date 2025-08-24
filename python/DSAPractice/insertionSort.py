import random
import matplotlib.pyplot as plt


def insertion_sort_visual(data):
    plt.ion()  # turn on interactive mode
    fig, ax = plt.subplots()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            ax.clear()
            ax.bar(range(len(data)), data, color="skyblue")
            ax.set_title(f"Insertion Sort Step {i}")
            plt.pause(0.01)  # pause to create animation effect
        data[j + 1] = key

    plt.ioff()
    plt.show()
    return data


def main():
    data_size = 30  # keep small so visualization is clear
    data = [random.randint(1, 100) for _ in range(data_size)]
    print("Unsorted:", data)
    sorted_data = insertion_sort_visual(data)
    print("Sorted:", sorted_data)


if __name__ == "__main__":
    main()
