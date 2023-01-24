import threads.listener
import threads.message
import threads.standby

key_listener = threads.listener.Listener()
watchdog = threads.standby.WatchDog()
message_server = threads.message.Server()


def start_threads():
    if not key_listener.started:
        key_listener.start()

    if not watchdog.started:
        watchdog.start()

    if not message_server.started:
        message_server.start()
