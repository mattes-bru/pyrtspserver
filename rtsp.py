#!/usr/bin/env python3
# -*- coding:utf-8 vi:ts=4:noexpandtab
# Simple RTSP server. Run as-is or with a command-line to replace the default pipeline

import sys
import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib

loop = GLib.MainLoop()
Gst.init(None)

class VideoFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        GstRtspServer.RTSPMediaFactory.__init__(self)

    def do_create_element(self, url):
        pipeline_str = "( v4l2src ! video/x-h264,width=1280,height=720,framerate=30/1,profile=high ! rtph264pay name=pay0 pt=96 )" # Use camera h264
        return Gst.parse_launch(pipeline_str)


class AudioFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        GstRtspServer.RTSPMediaFactory.__init__(self)

    def do_create_element(self, url):
        print("Creating element for:" , url)
        pipeline_str = "( alsasrc ! queue ! mulawenc ! rtppcmupay name=pay0 )"
        return Gst.parse_launch(pipeline_str)


class GstServer():
    def __init__(self):
        self.server = GstRtspServer.RTSPServer()

        vid_fact = VideoFactory()
        vid_fact.set_shared(True)

        aud_fact = AudioFactory()
        aud_fact.set_shared(True)

        m = self.server.get_mount_points()
        m.add_factory("/video", vid_fact)
        m.add_factory("/audio", aud_fact)
        self.server.attach(None)

if __name__ == '__main__':
    s = GstServer()
    loop.run()

