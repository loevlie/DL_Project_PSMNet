import matplotlib.pyplot as plt 

"""
Plot the results obtained from experiments.
"""
def main():
    ####################################################
    ############### INITIALIZE VARIABLES ###############
    ####################################################

    # Midterm Experiments
    original_path = "data/original.txt"
    increased_path = "data/increased.txt"
    decreased_path = "data/decreased.txt"
    reduced_parameter_path = "data/reduced_parameter.txt"

    # Final Experiments
    ir_base_path = "data/ir_base.txt"
    ir_shreyas_path = "data/ir_decrease_shreyas.txt"
    ir_josh_path = "data/ir_increase_josh.txt"
    reduced_parameter_full_path = "data/v1_rgb.txt"
    further_reduced_parameter_path = "data/v2_rgb.txt"

    # Final RGB results
    psmnet_rgb_path = "data/psmnet_rgb.txt"
    baseline_rgb_path = "data/midterm_baseline_rgb.txt"
    v1_rgb_path = "data/v1_rgb.txt"
    v2_rgb_path = "data/v2_rgb.txt"
    final_model_rgb_path = "data/final_model_rgb.txt"

    # Final IR results
    psmnet_ir_path = "data/psmnet_ir.txt"
    baseline_ir_path = "data/midterm_baseline_ir.txt"
    v1_ir_path = "data/v1_ir.txt"
    v2_ir_path = "data/v2_ir.txt"
    final_model_ir_path = "data/final_model_ir.txt"

    # Initialize the data arrays
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
    ir_base_loss = []
    ir_base_time = []
    ir_base_acc = []
    ir_shreyas_loss = []
    ir_shreyas_time = []
    ir_shreyas_acc = []
    ir_josh_loss = []
    ir_josh_time = []
    ir_josh_acc = []
    reduced_param_full_loss = []
    reduced_param_full_time = []
    reduced_param_full_acc = []
    further_reduced_param_loss = []
    further_reduced_param_time = []
    further_reduced_param_acc = []

    # RGB data arrays
    psmnet_rgb_loss, psmnet_rgb_time, psmnet_rgb_acc = [], [], []
    baseline_rgb_loss, baseline_rgb_time, baseline_rgb_acc = [], [], []
    v1_rgb_loss, v1_rgb_time, v1_rgb_acc = [], [], []
    v2_rgb_loss, v2_rgb_time, v2_rgb_acc = [], [], []
    final_rgb_loss, final_rgb_time, final_rgb_acc = [], [], []

    # IR data arrays
    psmnet_ir_loss, psmnet_ir_time, psmnet_ir_acc = [], [], []
    baseline_ir_loss, baseline_ir_time, baseline_ir_acc = [], [], []
    v1_ir_loss, v1_ir_time, v1_ir_acc = [], [], []
    v2_ir_loss, v2_ir_time, v2_ir_acc = [], [], []
    final_ir_loss, final_ir_time, final_ir_acc = [], [], []

    ####################################################
    ################# READ IN THE DATA #################
    ####################################################

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

    file5 = open(ir_base_path, 'r')
    count = 0
    for line in file5:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            ir_base_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            ir_base_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            ir_base_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    file6 = open(ir_shreyas_path, 'r')
    count = 0
    for line in file6:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            ir_shreyas_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            ir_shreyas_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            ir_shreyas_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    file7 = open(ir_josh_path, 'r')
    count = 0
    for line in file7:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            ir_josh_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            ir_josh_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            ir_josh_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    file8 = open(reduced_parameter_full_path, 'r')
    count = 0
    for line in file8:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            reduced_param_full_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            reduced_param_full_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            reduced_param_full_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    file9 = open(further_reduced_parameter_path, 'r')
    count = 0
    for line in file9:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            further_reduced_param_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            further_reduced_param_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            further_reduced_param_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the PSMNet RGB data
    file10 = open(psmnet_rgb_path, 'r')
    count = 0
    for line in file10:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            psmnet_rgb_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            psmnet_rgb_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            psmnet_rgb_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the Baseline RGB data
    file11 = open(baseline_rgb_path, 'r')
    count = 0
    for line in file11:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            baseline_rgb_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            baseline_rgb_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            baseline_rgb_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the v1 RGB data
    file12 = open(v1_rgb_path, 'r')
    count = 0
    for line in file12:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            v1_rgb_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            v1_rgb_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            v1_rgb_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the v2 RGB data
    file13 = open(v2_rgb_path, 'r')
    count = 0
    for line in file13:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            v2_rgb_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            v2_rgb_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            v2_rgb_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the final model RGB data
    file14 = open(final_model_rgb_path, 'r')
    count = 0
    for line in file14:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            final_rgb_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            final_rgb_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            final_rgb_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the PSMNet IR data
    file14 = open(psmnet_ir_path, 'r')
    count = 0
    for line in file14:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            psmnet_ir_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            psmnet_ir_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            psmnet_ir_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the Baseline IR data
    file15 = open(baseline_ir_path, 'r')
    count = 0
    for line in file15:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            baseline_ir_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            baseline_ir_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            baseline_ir_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the v1 IR data
    file16 = open(v1_ir_path, 'r')
    count = 0
    for line in file16:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            v1_ir_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            v1_ir_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            v1_ir_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the v2 IR data
    file17 = open(v2_ir_path, 'r')
    count = 0
    for line in file17:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            v2_ir_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            v2_ir_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            v2_ir_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    # Read in the final model IR data
    file18 = open(final_model_ir_path, 'r')
    count = 0
    for line in file18:
        s = line.strip()
        if count == 1:
            num = float(s[s.find(':')+2:])
            final_ir_loss.append(num)
        elif count == 2:
            num = float(s[s.find(':')+2:])
            final_ir_time.append(num)
        elif count == 3:
            num = float(s[s.find(':')+2:])
            final_ir_acc.append(num)
        elif count == 4:
            count = -1
        count += 1

    ####################################################
    ################# PLOT THE RESULTS #################
    ####################################################


    # # plot the loss for the midterm report
    # basic, = plt.plot(original_loss, label='PSMNet implementation')
    # increased, = plt.plot(increased_loss, label='increased conv layers')
    # decreased, = plt.plot(decreased_loss, label='decreased conv layers')
    # reduced, = plt.plot(reduced_param_loss, label='reduced params')
    # plt.title('L1 Loss (RGB)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("midterm_loss.png")

    # # plot the accuracy for the midterm report
    # basic, = plt.plot(original_acc, label='PSMNet implementation')
    # increased, = plt.plot(increased_acc, label='increased conv layers')
    # decreased, = plt.plot(decreased_acc, label='decreased conv layers')
    # reduced, = plt.plot(reduced_param_acc, label='reduced params')
    # plt.title('3-pixel Accuracy (RGB)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Accuracy (%)')
    # plt.legend(loc='lower right')
    # plt.savefig("midterm_accuracy.png")

    # plot the loss for the feature extraction layer experiments
    # ir_base, = plt.plot(ir_base_loss, label='baseline model')
    # shreyas, = plt.plot(ir_shreyas_loss, label='decreased feature extraction layers')
    # josh, = plt.plot(ir_josh_loss, label='increased feature extraction layers')
    # plt.title('L1 Loss (IR)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("feature_extraction_experiment_loss.png")

    # # plot the accuracy for the feature extraction layer experiments
    # ir_base, = plt.plot(ir_base_acc, label='baseline model')
    # shreyas, = plt.plot(ir_shreyas_acc, label='decreased feature extraction layers')
    # josh, = plt.plot(ir_josh_acc, label='increased feature extraction layers')
    # plt.title('3-pixel Accuracy (IR)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Accuracy (%)')
    # plt.legend(loc='lower right')
    # plt.savefig("feature_extraction_experiment_acc.png")

    # plot the loss
    # reduced, = plt.plot(reduced_param_full_loss, label='initial reduced param')
    # further_reduced, = plt.plot(further_reduced_param_loss, label='further reduced param')
    # plt.title('L1 Loss')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("param_reduction_loss.png")

    # # plot the time
    # reduced, = plt.plot(reduced_param_full_time, label='initial reduced param')
    # further_reduced, = plt.plot(further_reduced_param_time, label='further reduced param')
    # plt.title('Train Time')
    # plt.xlabel('Epochs')
    # plt.ylabel('Time (min)')
    # plt.legend()
    # plt.savefig("param_reduction_time.png")

    # # plot the accuracy
    # reduced, = plt.plot(reduced_param_full_acc, label='initial reduced param')
    # further_reduced, = plt.plot(further_reduced_param_acc, label='further reduced param')
    # plt.title('3-pixel Accuracy')
    # plt.xlabel('Epochs')
    # plt.ylabel('Accuracy (%)')
    # plt.legend()
    # plt.savefig("param_reduction_acc.png")

    # plot the loss for the final report (RGB)
    # psmnet_rgb, = plt.plot(psmnet_rgb_loss, label='PSMNet implementation')
    # baseline_rgb, = plt.plot(baseline_rgb_loss, label='baseline model')
    # v1_rgb, = plt.plot(v1_rgb_loss, label='v1 reduced param')
    # v2_rgb, = plt.plot(v2_rgb_loss, label='v2 reduced param')
    # final_rgb, = plt.plot(final_rgb_loss, label='final model')
    # plt.title('L1 Loss (RGB)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("rgb_loss.png")

    # # plot the time for the final report (RGB)
    # psmnet_rgb, = plt.plot(psmnet_rgb_time, label='PSMNet implementation')
    # baseline_rgb, = plt.plot(baseline_rgb_time, label='baseline model')
    # v1_rgb, = plt.plot(v1_rgb_time, label='v1 reduced param')
    # v2_rgb, = plt.plot(v2_rgb_time, label='v2 reduced param')
    # final_rgb, = plt.plot(final_rgb_time, label='final model')
    # plt.title('Train Time (RGB)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Time (min)')
    # plt.legend(loc='lower right')
    # plt.savefig("rgb_time.png")

    # # plot the accuracy for the final report (RGB)
    psmnet_rgb, = plt.plot(psmnet_rgb_acc, label='PSMNet implementation')
    baseline_rgb, = plt.plot(baseline_rgb_acc, label='baseline model')
    v1_rgb, = plt.plot(v1_rgb_acc, label='v1 reduced param')
    v2_rgb, = plt.plot(v2_rgb_acc, label='v2 reduced param')
    final_rgb, = plt.plot(final_rgb_acc, label='final model')
    plt.title('3-pixel Accuracy (RGB)')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.legend(loc='lower right')
    plt.savefig("rgb_acc.png")

    # plot the loss for the final report (IR)
    # psmnet_ir, = plt.plot(psmnet_ir_loss, label='PSMNet implementation')
    # baseline_ir, = plt.plot(baseline_ir_loss, label='baseline model')
    # v1_ir, = plt.plot(v1_ir_loss, label='v1 reduced param')
    # v2_ir, = plt.plot(v2_ir_loss, label='v2 reduced param')
    # final_ir, = plt.plot(final_ir_loss, label='final model')
    # plt.title('L1 Loss (IR)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.savefig("ir_loss.png")

    # plot the time for the final report (IR)
    # psmnet_ir, = plt.plot(psmnet_ir_time, label='PSMNet implementation')
    # baseline_ir, = plt.plot(baseline_ir_time, label='baseline model')
    # v1_ir, = plt.plot(v1_ir_time, label='v1 reduced param')
    # v2_ir, = plt.plot(v2_ir_time, label='v2 reduced param')
    # final_ir, = plt.plot(final_ir_time, label='final model')
    # plt.title('Train Time (IR)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Time (min)')
    # plt.legend(loc='lower right')
    # plt.savefig("ir_time.png")

    # plot the accuracy for the final report (IR)
    # psmnet_ir, = plt.plot(psmnet_ir_acc, label='PSMNet implementation')
    # baseline_ir, = plt.plot(baseline_ir_acc, label='baseline model')
    # v1_ir, = plt.plot(v1_ir_acc, label='v1 reduced param')
    # v2_ir, = plt.plot(v2_ir_acc, label='v2 reduced param')
    # final_ir, = plt.plot(final_ir_acc, label='final model')
    # plt.title('3-pixel Accuracy (IR)')
    # plt.xlabel('Epochs')
    # plt.ylabel('Accuracy (%)')
    # plt.legend(loc='lower right')
    # plt.savefig("ir_acc.png")

if __name__ == "__main__":
    main()