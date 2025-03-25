import uvicorn
import signal
import sys


def signal_handler(sig, frame):
    print("\nShutting down server gracefully...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n Server stopped by user")
    finally:
        print("Server shutdown complete")
