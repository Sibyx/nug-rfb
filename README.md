# nug-vnc

**Work in progress!**

Simple implementation of the VNC server (RFB protocol) based on the
[asyncio](https://docs.python.org/3/library/asyncio-protocol.html) module and the
[rfbproto](https://github.com/rfbproto/rfbproto) specification.

This project is a part of my master thesis on the
[Faculty of Informatics and Information Technologies STU in Bratislava](https://www.fiit.stuba.sk/en.html) on the
subject of KVM switch implementation.

We use [Poetry](https://python-poetry.org/) as a package manager.

## Credits

My implementation is heavily inspired by [rdpy](https://github.com/citronneur/rdpy) and
[pikvm](https://github.com/pikvm/kvmd) projects. I have especially enjoyed reading the implementation of the [typing
system in rdpy](https://github.com/citronneur/rdpy/blob/master/rdpy/core/type.py) and custom implementation of the
[RFB server in pikvm](https://github.com/pikvm/kvmd/tree/master/kvmd/apps/vnc).

---
With ❤️ and ☕️ Jakub Dubec 2021
