#!/usr/bin/env python3
# -*- coding:utf-8 vi:ts=4:noexpandtab

from factory import AudioFactory, VideoFactory
import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib


loop = GLib.MainLoop()
Gst.init(None)




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


def main():
    s = GstServer()
    loop.run()

if __name__ == '__main__':
    main()


