from __future__ import print_function, division
from StdSuites.Type_Names_Suite import point

__author__ = 'george'

import matplotlib.pyplot as plt
import numpy as np
from lib import *


COLORS = ['indigo', 'gold', 'hotpink', 'firebrick', 'indianred', 'yellow', 'mistyrose',
          'darkolivegreen', 'olive', 'darkseagreen', 'pink', 'tomato', 'lightcoral',
          'orangered', 'navajowhite', 'lime', 'palegreen', 'greenyellow', 'burlywood',
          'seashell', 'mediumspringgreen', 'fuchsia', 'papayawhip', 'blanchedalmond',
          'chartreuse', 'dimgray', 'black', 'peachpuff', 'springgreen', 'aquamarine',
          'white', 'orange', 'lightsalmon', 'darkslategray', 'brown', 'ivory',
          'dodgerblue', 'peru', 'lawngreen', 'chocolate', 'crimson', 'forestgreen',
          'slateblue', 'lightseagreen', 'cyan', 'mintcream', 'silver', 'antiquewhite',
          'mediumorchid', 'skyblue', 'gray', 'darkturquoise', 'goldenrod', 'darkgreen',
          'floralwhite', 'darkviolet', 'darkgray', 'moccasin', 'saddlebrown', 'darkslateblue',
          'lightskyblue', 'lightpink', 'mediumvioletred', 'red', 'deeppink', 'limegreen',
          'darkmagenta', 'palegoldenrod', 'plum', 'turquoise', 'lightgoldenrodyellow',
          'darkgoldenrod', 'lavender', 'maroon', 'yellowgreen', 'sandybrown', 'thistle',
          'violet', 'navy', 'magenta', 'tan', 'rosybrown', 'olivedrab', 'blue', 'lightblue',
          'ghostwhite', 'honeydew', 'cornflowerblue', 'linen', 'darkblue', 'powderblue',
          'seagreen', 'darkkhaki', 'snow', 'sienna', 'mediumblue', 'royalblue', 'lightcyan',
          'green', 'mediumpurple', 'midnightblue', 'cornsilk', 'paleturquoise', 'bisque',
          'slategray', 'darkcyan', 'khaki', 'wheat', 'teal', 'darkorchid', 'deepskyblue',
          'salmon', 'darkred', 'steelblue', 'palevioletred', 'lightslategray', 'aliceblue',
          'lightgreen', 'orchid', 'gainsboro', 'mediumseagreen', 'lightgray', 'mediumturquoise',
          'lemonchiffon', 'cadetblue', 'lightyellow', 'lavenderblush', 'coral', 'purple',
          'aqua', 'whitesmoke', 'mediumslateblue', 'darkorange', 'mediumaquamarine',
          'darksalmon', 'beige', 'blueviolet', 'azure', 'lightsteelblue', 'oldlace']


def get_colors(n):
  return sample(COLORS, n)

def plot_clusters(clusters, fig_name="temp.png", col_names=None, colors=None, **settings):
  """
  :param clusters: Key value pair of cluster_id and points in them
  :return:
  """
  if len(clusters.values()[0][0]) != 2:
    raise RuntimeError(500, "Only 2 dimensional points supported")
  seed()
  if not col_names:
    col_names = ["Obj 1", "Obj 2"]
  if not colors:
    colors = get_colors(len(clusters.keys()))
  handles=[]
  cluster_labels = []
  size = 0
  for color, key in zip(colors, clusters.keys()):
    points = np.array(clusters.get(key))
    size += len(points)
    handles.append(plt.scatter(points[:,0], points[:,1], c=color, **settings))
    cluster_labels.append("cluster "+str(key))
  plt.xlabel(col_names[0])
  plt.ylabel(col_names[1])
  plt.legend(handles, cluster_labels)
  plt.savefig(fig_name)
  plt.clf()

def bar_plot(vals, fig_name="temp.png", label=None, **settings):
  ind = np.arange(len(vals.keys()))
  width = 0.35
  fig = plt.figure()
  fig.subplots_adjust(left=0.35)
  ax = fig.add_subplot(111)
  ax.barh(ind, vals.values(), width, color='r')
  if not label:
    label = "Time (in seconds)"
  ax.set_xlabel(label)
  ax.set_ylabel("Models")
  ax.set_yticks(ind)
  ax.set_yticklabels(vals.keys())
  # We change the fontsize of minor ticks label
  ax.tick_params(axis='both', which='major', labelsize=8)
  ax.tick_params(axis='both', which='minor', labelsize=7)
  plt.savefig(fig_name)
  plt.clf()