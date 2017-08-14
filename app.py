import web
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


urls = (

    '/read', 'read',
    '/write', 'write',
    '/setup', 'setup'

)
app = web.application(urls, globals())

class setup:
    def GET(self):
        get_data=web.input(p="17", s="out")
        pin = int(get_data.p)
        state = get_data.s
        if state == "out":
            GPIO.setup(pin, GPIO.OUT)
        if state == "in":
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        return str(pin)+" set to "+ state

class write:
    def GET(self):
        get_data=web.input(p="17", s="0")
        printout = "NO DATA"
        pin = int(get_data.p)
        state = int(get_data.s)
        GPIO.output(pin, state)
        printout = "<p>"+str(pin)+" set to "+str(state)+"</p>"
        return printout

class read:
	def GET(self):
		get_data=web.input(p="17")
		printout = "NO DATA"
		pin = int(get_data.p)
		return str(GPIO.input(pin))

if __name__ == "__main__":
    app.run()
