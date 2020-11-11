import matplotlib.pyplot as plt 

def main():
    """
    Plot the results obtained from our initial experiments to aid in baseline model development.
    """
    original_path = "data/original.txt"
    increased_path = "data/increased.txt"
    decreased_path = "data/decreased.txt"
    reduced_parameter_path = "data/reduced_parameter.txt"

    original_loss = []
    original_time = []
    original_acc = []
    increased_loss = []
    increased_time = []
    increased_acc = []
    decreased_loss = []
    decreased_time = []
    decreased_acc = []
    reduced_param_loss = []
    reduced_param_time = []
    reduced_param_acc = []

    file1 = open(original_path, 'r')
    count = 0
    for line in file1:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            original_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            original_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            original_acc.append(num)
        elif count == 4:
            count = -1

        count += 1

    file2 = open(increased_path, 'r')
    count = 0
    for line in file2:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            increased_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            increased_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            increased_acc.append(num)
        elif count == 4:
            count = -1

        count += 1

    file3 = open(reduced_parameter_path, 'r')
    count = 0
    for line in file3:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            reduced_param_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            reduced_param_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            reduced_param_acc.append(num)
        elif count == 4:
            count = -1

        count += 1

    file4 = open(decreased_path, 'r')
    count = 0
    for line in file4:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            decreased_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            decreased_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            decreased_acc.append(num)
        elif count == 4:
            count = -1

        count += 1

    # # plot the loss
    # basic, = plt.plot(original_loss, label='basic model')
    # increased, = plt.plot(increased_loss, label='increased conv layers')
    # decreased, = plt.plot(decreased_loss, label='decreased conv layers')
    # reduced, = plt.plot(reduced_param_loss, label='reduced params')
    # plt.title('L1 Loss')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("plot_loss.png")

    # plot the accuracy
    basic, = plt.plot(original_acc, label='basic model')
    increased, = plt.plot(increased_acc, label='increased conv layers')
    decreased, = plt.plot(decreased_acc, label='decreased conv layers')
    reduced, = plt.plot(reduced_param_acc, label='reduced params')
    plt.title('3-pixel Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.legend(loc='lower right')
    plt.savefig("plot_accuracy.png")

if __name__ == "__main__":
    main()