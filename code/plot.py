__author__ = 'Marcelo d\'Almeida'

import os

import matplotlib

matplotlib.use('Agg')
import code.learning.util as util
import matplotlib.pyplot as pyplot
import numpy as np
import math


def decisions(decision_per_time_info, available_decision_per_time_info, epoch):

    pyplot.close('all')

    number_of_plots = 1

    f, axs = pyplot.subplots(number_of_plots, 1, figsize=(30, 5 * number_of_plots))
    f.subplots_adjust(hspace=0.6)

    ####################################################################################################

    axs1 = axs

    axs1.set_xlabel('Cumulative Power')
    axs1.set_ylabel('Actions')
    axs1.set_title('Decisions - Epoch ' + str(epoch))

    axs1.plot(available_decision_per_time_info[1], available_decision_per_time_info[0], 'rD', label="Available Decisions")
    axs1.plot(decision_per_time_info[1], decision_per_time_info[0], 'bD', label="Actual Decisions")
    axs1.set_yticks(range(0, 10))
    axs1.set_yticklabels([util.actions_dict[x] for x in range(0, 10)])
    axs1.set_xlim([-1, axs1.get_xlim()[1] + 1])
    axs1.set_ylim([-0.5, 9.5])

    axs1.axhline(y=6.5, color='k')
    axs1.axhline(y=3.5, color='k')
    axs1.axhline(y=0.5, color='k')

    axs1.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################


    newpath = './info/plot/' + 'decision' + '/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)



    pyplot.savefig('./info/plot/' + 'decision' + '/' + 'learning' + '_Decision' + str(epoch)+'.png')

def rewards(rewards_per_time_info, rewards_detailed_info, epoch):

    pyplot.close('all')

    number_of_plots = 5

    f, axs = pyplot.subplots(number_of_plots, 1, figsize=(30, 5 * number_of_plots))
    f.subplots_adjust(hspace=0.6)

    rewards_cost_detailed_info = rewards_detailed_info[0]
    rewards_time_detailed_info = rewards_detailed_info[1]

    axs1 = axs[0]
    axs2 = axs[1]
    axs3 = axs[2]
    axs4 = axs[3]
    axs5 = axs[4]

    ####################################################################################################

    axs1.set_xlabel('Cumulative Power')
    axs1.set_ylabel('Rewards')
    axs1.set_title('Rewards - Epoch ' + str(epoch))

    #axs[0].plot(rewards_per_time_info[1], rewards_per_time_info[2], 'rD', label="Number of tasks")
    axs1.plot(rewards_per_time_info[1], rewards_per_time_info[0], 'bD', label="Reward")

    axs1.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    axs2.set_xlabel('Cumulative Power')
    axs2.set_ylabel('Cost Reward')
    axs2.set_title('Cost Rewards Over Power Progression - Epoch ' + str(epoch))

    axs2.plot(rewards_cost_detailed_info[2], rewards_cost_detailed_info[3], 'bD', label="Cost Reward")

    axs2.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    axs3.set_xlabel('Cumulative Power')
    axs3.set_ylabel('Cost Measurement')
    axs3.set_title('Cost Measurements Over Power Progression - Epoch ' + str(epoch))

    axs3.plot(rewards_cost_detailed_info[2], rewards_cost_detailed_info[0], 'gD', label="Best measurement")
    axs3.plot(rewards_cost_detailed_info[2], rewards_cost_detailed_info[1], 'bD', label="Actual measurement")

    axs3.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    axs4.set_xlabel('Cumulative Power')
    axs4.set_ylabel('Time Reward')
    axs4.set_title('Time Rewards Over Power Progression - Epoch ' + str(epoch))

    axs4.plot(rewards_time_detailed_info[2], rewards_time_detailed_info[3], 'bD', label="Time Reward")

    axs4.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    axs5.set_xlabel('Cumulative Power')
    axs5.set_ylabel('Time Measurement')
    axs5.set_title('Time Measurements Over Power Progression - Epoch ' + str(epoch))

    axs5.plot(rewards_time_detailed_info[2], rewards_time_detailed_info[0], 'gD', label="Best measurement")
    axs5.plot(rewards_time_detailed_info[2], rewards_time_detailed_info[1], 'bD', label="Actual measurement")

    axs5.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    newpath = './info/plot/' + 'reward' + '/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    pyplot.savefig('./info/plot/' + 'reward' + '/' + 'learning' + '_Reward' + str(epoch)+'.png')

def distance_error(rewards_detailed_info, goal_info, epoch):

    pyplot.close('all')

    number_of_plots = 2

    f, axs = pyplot.subplots(number_of_plots, 1, figsize=(30, 5 * number_of_plots))
    f.subplots_adjust(hspace=0.6)

    rewards_cost_detailed_info = rewards_detailed_info[0]
    rewards_time_detailed_info = rewards_detailed_info[1]

    cost_goal = goal_info[0]
    time_goal = goal_info[1]

    cost_measurement = rewards_cost_detailed_info[1]
    if cost_goal > 0:
        best_cost = cost_goal
    else:
        best_cost = max(rewards_cost_detailed_info[0])

    for i in range(len(cost_measurement)):
        cost_measurement[i] = math.sqrt(pow(best_cost - cost_measurement[i], 2))

        if i != 0:
            cost_measurement[i] += cost_measurement[i-1]


    time_measurement = rewards_time_detailed_info[1]
    if time_goal > 0:
        best_time = time_goal
    else:
        best_time = max(rewards_time_detailed_info[0])

    for i in range(len(time_measurement)):
        time_measurement[i] = math.sqrt(pow(best_time - time_measurement[i], 2))

        if i != 0:
            time_measurement[i] += time_measurement[i-1]


    axs1 = axs[0]
    axs2 = axs[1]

    ####################################################################################################

    axs1.set_xlabel('Cumulative Power')
    axs1.set_ylabel('Cumulative Cost Distance Error')
    axs1.set_title('Cost Distance Error Over Power Progression - Epoch ' + str(epoch))


    axs1.plot(rewards_cost_detailed_info[2], cost_measurement, 'bD-', label="Cost Cumulative Error")

    axs1.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    axs2.set_xlabel('Cumulative Power')
    axs2.set_ylabel('Cumulative Time Distance Error')
    axs2.set_title('Time Distance Error Over Power Progression - Epoch ' + str(epoch))

    axs2.plot(rewards_time_detailed_info[2], time_measurement, 'bD-', label="Time Cumulative Error")

    axs2.legend(bbox_to_anchor=(1.002, 1), loc=2, borderaxespad=0., numpoints=1)

    ####################

    newpath = './info/plot/' + 'distance_error' + '/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    pyplot.savefig('./info/plot/' + 'distance_error' + '/' + 'learning' + '_Distance_Error' + str(epoch)+'.png')

def q_table(power_q_table, cost_q_table, delay_q_table, epoch):

    pyplot.close('all')

    number_of_plots = 3

    f, axs = pyplot.subplots(number_of_plots, 1, figsize=(30, 5 * number_of_plots))
    f.subplots_adjust(hspace=0.6)

    axs1 = axs[0]
    axs2 = axs[1]
    axs3 = axs[2]

    p = np.matrix(power_q_table)
    c = np.matrix(cost_q_table)
    d = np.matrix(delay_q_table)

    vmax = max([p.max(), c.max(), d.max()])
    vmin = min([p.min(), c.min(), d.min()])

    ticks = np.linspace(vmin, vmax, 20)

    ####################################################################################################

    left, width = .25, .5
    bottom, height = .50, .5
    right = left + width
    top = bottom + height

    axs1.set_xlabel('Actions')
    axs1.set_ylabel('Percentage')

    axs1.matshow(power_q_table, vmin=vmin, vmax=vmax, aspect='auto')

    pos = axs1.get_position()
    axs1.set_position([pos.x0 - 0.076, pos.y0,  pos.width + 0.09, pos.height])

    pos = axs1.get_position()
    axs1.text(pos.x0 + pos.width/2 + 0.02, pos.y0 + pos.height + 0.25,
        'Power Q-Table - Epoch ' + str(epoch),
        fontsize=18,
        horizontalalignment='center',
        transform=axs1.transAxes)

    axs1.set_xticks(range(0, 10))
    axs1.set_xticklabels([util.actions_dict[x] for x in range(0, 10)])
    axs1.set_yticks(range(0, 6))
    axs1.set_yticklabels([util.percentage_dict[x] for x in range(0, 6)])

    ####################

    axs2.set_xlabel('Actions')
    axs2.set_ylabel('Percentage')

    axs2.matshow(cost_q_table, vmin=vmin, vmax=vmax, aspect='auto')

    pos = axs2.get_position()
    axs2.set_position([pos.x0 - 0.076, pos.y0,  pos.width + 0.09, pos.height])

    pos = axs2.get_position()
    axs2.text(pos.x0 + pos.width/2 + 0.02, pos.y0 + pos.height + 0.55,
        'Cost Q-Table - Epoch ' + str(epoch),
        fontsize=18,
        horizontalalignment='center',
        transform=axs2.transAxes)

    axs2.set_xticks(range(0, 10))
    axs2.set_xticklabels([util.actions_dict[x] for x in range(0, 10)])
    axs2.set_yticks(range(0, 6))
    axs2.set_yticklabels([util.percentage_dict[x] for x in range(0, 6)])

    ####################

    axs3.set_xlabel('Actions')
    axs3.set_ylabel('Percentage')

    im = axs3.matshow(delay_q_table, vmin=vmin, vmax=vmax, aspect='auto')

    pos = axs3.get_position()
    axs3.set_position([pos.x0 - 0.076, pos.y0,  pos.width + 0.09, pos.height])

    pos = axs3.get_position()
    axs3.text(pos.x0 + pos.width/2 + 0.02, pos.y0 + pos.height + 0.85,
        'Delay Q-Table - Epoch ' + str(epoch),
        fontsize=18,
        horizontalalignment='center',
        transform=axs3.transAxes)

    axs3.set_xticks(range(0, 10))
    axs3.set_xticklabels([util.actions_dict[x] for x in range(0, 10)])
    axs3.set_yticks(range(0, 6))
    axs3.set_yticklabels([util.percentage_dict[x] for x in range(0, 6)])

    ####################

    cax = f.add_axes([0.93, 0.1, 0.03, 0.8])
    pyplot.colorbar(im, cax=cax, ticks=ticks)

    newpath = './info/plot/' + 'q_table' + '/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    pyplot.savefig('./info/plot/' + 'q_table' + '/' + 'learning' + '_Q_Table' + str(epoch)+'.png')