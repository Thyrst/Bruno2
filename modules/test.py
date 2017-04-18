class test(object):

    def on_server_connected(self):
        self.join('#testbruno')

    def on_channel_message(self, chan_name, nickname, hostname, msg):
        print 'To: ' + chan_name
        print 'From: ' + nickname
        print 'Msg: ' + msg
        print ''

        self.send_msg(chan_name, msg)
