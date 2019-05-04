class SLU():
    intent = ""

    def analyze(self, message):
        if ('buy' in message) and ('fruit' in message):
            self.intent = 'buy fruit'
            return self.intent
        elif ('pay' in message):
            self.intent = 'pay'
            return self.intent