"""
Copyright (c) 2022 Julien Posso
"""

import matplotlib.pyplot as plt
import os
folder_path = "C:/Users/Mama/Desktop/projtake3/Mobile-URSONet-master/display/exp"
def print_training_loss(loss, show=False, save=True):
    plt.figure()
    # plt.title("Loss")
    plt.plot(loss['train'], label='train')
    plt.plot(loss['valid'], label='valid')
    plt.xlabel('Epoch')
    plt.ylabel('Average loss')
    plt.legend()

    if show:
        plt.show()

    if save:
        plt.savefig(os.path.join(folder_path, "train_valid_loss.png"))

    plt.close()


def print_training_score(score, show=False, save=True):
    plt.figure()
    # plt.title("ESA score on validation set")
    plt.plot(score['valid']['ori'], label='orientation')
    plt.plot(score['valid']['pos'], label='position')
    plt.plot(score['valid']['esa'], label='ESA')
    plt.xlabel('Epoch')
    plt.ylabel('Score')
    plt.legend()

    if show:
        plt.show()

    if save:
        plt.savefig(os.path.join(folder_path, "score.png"))

    plt.close()


def print_beta_tuning(beta_list, score, show=False, save=True):
    plt.figure()
    # plt.title("Effect of Beta hyperparameter on ESA score")
    plt.plot(beta_list, score['ori'], label='orientation')
    plt.plot(beta_list, score['pos'], label='position')
    plt.plot(beta_list, score['esa'], label='ESA')
    plt.ylabel('Score')
    plt.xlabel('Beta value')
    plt.legend()

    if show:
        plt.show()

    if save:
        plt.savefig(os.path.join(folder_path, "score_bet a_tuning.png"))

    plt.close()


def print_error_distance(ori_err, pos_err, distance, show=False, save=True):

    fig, (ax1, ax2) = plt.subplots(2)
    # fig.suptitle('Error by distance')
    ax1.plot(distance, ori_err, 'b.')
    ax2.plot(distance, pos_err, 'b.')
    ax1.set_ylabel('Orientation error (deg)')
    ax2.set_ylabel('Position error (m)')
    ax2.set_xlabel('Distance with target spacecraft (m)')

    if show:
        plt.show()

    if save:
        plt.savefig(os.path.join(folder_path, "error_by_distance.png"))

    plt.close()
