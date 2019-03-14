#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: data_show.py
@time: 2019/03/14
"""
import plotly.offline as pyoff
import plotly.graph_objs as go
import numpy as np


class Plt(object):
    """
    show data with plotly
    """

    def __init__(self):
        pass

    def load_data(self, data):
        self._data = data

    def plot(self, **kwargs):
        w, b = kwargs['w'], kwargs['b']
        date = []
        open = []
        high = []
        low = []
        close = []
        line_scatters = []
        _x = 0
        for item in self._data:
            date.append(item['DATE'])
            open.append(item['TOPEN'])
            high.append(item['HIGH'])
            low.append(item['LOW'])
            close.append(item['TCLOSE'])
            line_scatters.append(w * _x + b)
            _x += 1

        trace = go.Ohlc(x=date,
                        open=open,
                        high=high,
                        low=low,
                        close=close,
                        increasing=dict(line=dict(color='red')),
                        decreasing=dict(line=dict(color='green')),
                        showlegend=False)

        line = go.Scatter(
            x=date,
            y=line_scatters,
            mode='lines+markers',
            name='Regression',
            showlegend=False,
        )

        data = [trace, line]
        pyoff.plot(data)
