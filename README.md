# Simple RTSP Server written in Python using GStreamer


## Dependencies

### macOS

Using Homebrew 🍺:

```bash
brew install gstreamer gstreamer-rtspserver
```

## Configuration

Pipeline for a webcam with h264 support
```
v4l2src ! video/x-h264,width=1280,height=720,framerate=30/1,profile=high ! rtph264pay name=pay0 pt=96
```

Pipeline for audio only streaming
```
alsasrc ! queue ! mulawenc ! rtppcmupay name=pay0
```

