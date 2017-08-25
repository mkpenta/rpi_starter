We had 5 students attend the first three nights. Three students attended the fourth night. Two students attended all nights. 
All but one student brought their own RasPi
 - Anthony M attended 5 nights, CIS Trnasfer, 2nd year
 - James D attended 5 nights, CIS Trnasfer, 2nd year
 - Tony G attended 4 nights, Mechanical Engineering, new student
 - Tony attended 3 nights (also attended ethel's workshop)
 - J Carlos attended 3 nights, biology, finishing NECC and attending UMASS amherst in the fall.
 
 The first two nights Jason D assisted in both instructional and technical support. 
 
 
**Topics Each Night**
 1. RPi setup
  On this night the students set up the raspberry pis by downloading ant installing the image (we used Raspian Stretch Lite on 4GB SD and used a command line for most tasks). I set a goal to have the RPis setup to automatically connect to the wireless network in the lab, be capable of accessing the the RPi through ssh, and creating a hostname to allow for connection without knowledge of the IP. This can be done headlessly (without a monitor and keyboard, see workshopNotes.txt) but we connected the RPis to lab monitors and keyboards and changed the settings using raspi-config. We concluded the evening by discussing the powerful tool apt-get and using apt-get to install the components of a LAMP server.
 
2. After installing the LAMP server, we created very simple HTML files to display a webpage hosted on the RPi. Student could open up any browser in the lab and vist http://hostname.local to view the page. I provided some sample HTML, CSS, and PHP in order to test the PHP setup.nLater in the evening we wired an LED to the Pi using the PiCobbler (students with their own RPi3s needed female to male header wires). We tested our circuit with programs in C and in Python. The programs turned the lights on and then off.

3. This was the last night of organized instruction. The following two nights were intended for supportive exporloration of student driven topics. This evening we first discussed input and output on the pins. We had a visit from a representiative evaluating the bootcamp and spent some time speaking with her about our content and student experiences. After we constructed circuits that included buttons and LEDs. Students were given some sample code to respond to the button. Then students worked combining the light code and the button code to create a program that turned a light on in response to a button. Lastly sample code was provided to show students how python could act as a web server to create a GPIO API for the RPI. 

4. Two students teamed up to work on an application that used a camera to take a picture and post it on the RPi hosted web page. One student works to set up a retro gaming station on his personal RPi.

5. Two students try to expand their project to take a picture and use facial recognition to bring a user to a specific webpage. 
 
In all, student seemed motivated and excited to learn about the pi. 
