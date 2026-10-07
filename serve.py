#!/usr/bin/env python3
"""Serve ONLY ./serve on the LAN, with caching disabled.

Two reasons this exists instead of a bare `python3 -m http.server`:
  1. http.server serves its whole working directory. Run from the project root
     it would expose rsi-trader/ (bot source, config.yaml, .env*) to anyone on
     the network. Serving ./serve, which holds a single symlink to the
     dashboard, keeps everything else unreachable.
  2. http.server sends Last-Modified but no Cache-Control, so browsers — phones
     especially — keep serving a stale copy after the dashboard is edited.
     no-store forces a fresh fetch every load.
"""
import http.server, os, socket, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "serve")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8777


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


if __name__ == "__main__":
    host = socket.gethostname().split(".")[0]
    print(f"serving {ROOT}")
    print(f"  this Mac : http://localhost:{PORT}")
    print(f"  phone    : http://{lan_ip()}:{PORT}")
    print(f"  or       : http://{host}.local:{PORT}")
    print("  Ctrl-C to stop")
    http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
