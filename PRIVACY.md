# Privacy Policy for Phantom Lyrics - YouTube Timestamp

**Last updated: June 25, 2026**

## Overview

Phantom Lyrics - YouTube Timestamp is a Firefox extension that works with the Phantom Lyrics desktop application to display synchronized lyrics on your screen while you listen to music on YouTube.

## What Data We Access

The extension reads the following information **from the YouTube page you are viewing**:

- **Page title** (`document.title`) — used to identify the currently playing song (artist and title)
- **Video playback position** (`video.currentTime`) — used to sync lyrics with the audio
- **Video duration** (`video.duration`) — informational
- **Playback state** (`video.paused`) — whether the video is playing or paused

## Where the Data Goes

All data is sent **exclusively to your own computer** via a local WebSocket connection to `ws://localhost:8765`. This is the Phantom Lyrics desktop application running on your machine.

**The data never leaves your computer.** It is not sent to any external server, cloud service, third party, or the extension developer. There is no remote backend.

## What We Do Not Do

This extension:

- ❌ Does **not** collect, store, or transmit personal information
- ❌ Does **not** send data to any external server or third party
- ❌ Does **not** use analytics, tracking pixels, or telemetry
- ❌ Does **not** serve advertising
- ❌ Does **not** read or modify any data outside YouTube pages
- ❌ Does **not** access your browsing history, cookies, passwords, or bookmarks
- ❌ Does **not** collect data from pages other than YouTube

## Data Storage

The extension **does not store any data**. All data is read in real-time from the page and immediately sent to the local desktop application. No data is written to browser storage, cookies, or local files.

## Permissions Explained

- `*://*.youtube.com/*` — The extension only runs on YouTube pages. It needs this permission to read the video playback position for lyrics synchronization.

## Contact

For questions about this privacy policy, please open an issue at:
https://github.com/Anngiie/PhantomLyrics/issues
