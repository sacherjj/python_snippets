__author__ = "Joe Sacher <sacherjj@gmail.com>"


from circuits import Component, Event, handler, Timer, Debugger


class event_with_data(Event):
    """Hopefully we can send data with this!"""


class event_workflow_process(Event):
    """Called to process next step in workflow"""


class event_shutdown(Event):
    """Can I shutdown with this?"""


class Receiver(Component):
    def init(self, channel):
        self.channel = channel
        print('Receiver Initialized {}'.format(self.channel))

    @handler('event_with_data')
    def get_data(self, event, *args, **kwargs):
        print('received {} on {}'.format(str(kwargs), self.channel))
        event.stop()


class Ticker(Component):
    def init(self, parent):
        pass
        self.channel = 'ticker'

    def process_workflow(self):
        print('workflow')


class Sender(Component):
    def init(self):
        self.channel = 'sender'
        self.tick_count = 0
        print('Sender Initialized')
        Debugger().register(self)
        Receiver('a').register(self)
        Receiver('b').register(self)
        Ticker(self).register(self)

    def send_data(self, chan, **kwargs):
        print('sending data {}'.format(str(kwargs)))
        my_event = event_with_data(success=True, complete=True, **kwargs)
        self.fire(my_event, chan)
#        print(my_event.value)
#        self.fire(event_with_data(**{'ha': 'b deserves no data'}), 'b')

    @handler('event_shutdown')
    def shutdown_now(self, event, *args, **kwargs):
        print('shutdown')
        self.stop()

    @handler('event_with_data')
    def get_data(self, event, *args, **kwargs):
        print('sender {}'.format(str(kwargs)))

    @handler('event_with_data_success')
    def processed(self, event, *args, **kwargs):
        print('processed args:{} kwargs:{}'.format(str(args), str(kwargs)))


send = Sender()
Timer(15, event_shutdown(), 'sender').register(send)
send.send_data('a', joe='confused')
send.send_data('b', value={'whatever': {1: 2, 5: [1, 2, 3, 4, 5]}})
send.run()

