#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Digtal Modulation
# GNU Radio version: 3.9.4.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import channels
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class digital_mod_lab_full(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Digtal Modulation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Digtal Modulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "digital_mod_lab_full")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.qpsk = qpsk = digital.constellation_8psk().base()
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_lms( qpsk, .0001).base()
        self.taps = taps = 1
        self.samp_rate = samp_rate = 32000
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise = noise = 0.1
        self.freq_offset = freq_offset = 0
        self.delay = delay = 32

        ##################################################
        # Blocks
        ##################################################
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, "Phase: Bandwidth", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_bw_win)
        self._noise_range = Range(0, 1, 0.0001, 0.1, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "Noise", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_win)
        self._freq_offset_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self._delay_range = Range(0, 200, 1, 32, 200)
        self._delay_win = RangeWidget(self._delay_range, self.set_delay, "Delay", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
            512, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 2, 1, 2, 2)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "After Equalizer", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "Before Equalizer", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_map_bb_0 = digital.map_bb([0,1,2,3,4,5,6,7])
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, 8, False)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(qpsk)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(qpsk)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=noise,
            frequency_offset=freq_offset,
            epsilon=1,
            taps=[taps],
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(3)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(3)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/baser/Desktop/gr-ws/file.txt', True, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/baser/Desktop/gr-ws/file.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_constellation_encoder_bc_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "digital_mod_lab_full")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps([self.taps])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(self.delay)




def main(top_block_cls=digital_mod_lab_full, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
