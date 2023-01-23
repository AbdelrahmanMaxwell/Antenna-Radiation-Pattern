from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import time

# Use png images
from PIL import Image, ImageTk

main_window = Tk()
main_window.title("Antenna Radiation Pattern")
main_window.geometry("1215x700+250+200")
main_window.resizable(width=False, height=False)


def antennaGenerate():
    # Frame2
    frame2 = Frame(main_window)

    def dipole():
        frame2.destroy()
        # Frame3
        frame3 = Frame(main_window)

        def plot_dipole():
            # Linera Antenna [Dipole]

            freq = 10e6 # Set the operating frequency of the dipole in Hz
            wavelength = 3e8/freq # Calculate the wavelength of the signal

            lmda = 1
            d = float(Fraction(entry2.get()))   # Antenna Length
            beta = 2*np.pi/lmda; # bita
            phi = np.linspace(0, 2*np.pi, 1000)

            # Set the number of points to calculate the radiation pattern
            theta = np.linspace(0, 2*np.pi, 360)
            gamma=np.linspace(0,2*np.pi,360)
            #epsi=alpha+beta*d*np.cos(gamma);

            # Calculate the radiation pattern using the equation for a dipole antenna
            af= 60*((np.cos(beta*d*np.cos(phi)/2) - np.cos(beta*d/2)) / np.sin(phi))
            af=np.abs(af)

            # Plot the polar radiation pattern
            plt.figure(1)
            plt.plot(phi, af)
            plt.xlabel('Angle (radians)')
            plt.ylabel('Radiation pattern (dB)')
            plt.title('radiation pattern of a dipole antenna')

            fig = plt.figure(2)
            ax = fig.add_subplot(111, projection='polar')
            ax.plot(phi, af)
            ax.set_title('Polar radiation pattern of a dipole antenna')

            plt.show()

            # Fix Background BalckScreen
            Antenna_image2 = PhotoImage(file="bilder/emty.png")
            canvas2 = Canvas(frame3, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
            canvas2.create_image(0, 0, image=Antenna_image2, anchor=NW)

        def back_home():
            frame3.destroy()
            antennaGenerate()

        Antenna_image2 = PhotoImage(file="bilder/emty.png")
        canvas2 = Canvas(frame3, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
        canvas2.create_image(0, 0, image=Antenna_image2, anchor=NW)

        label1 = Label(frame3, text=" Write Antenna Parameters : ", bg="#5e4e3f", fg="white", relief="flat")

        label2 = Label(frame3, text=" Length(L) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry2 = Entry(frame3)

        button1 = Button(frame3, text=" Plot ", command=plot_dipole, bg="white", fg="black", relief="raised", activebackground="#f3951e")
        button2 = Button(frame3, text=" Back ", command=back_home, bg="white", fg="black", relief="raised", activebackground="#f3951e")

        frame3.place(x=0, y=0,width=1215, height=700)
        label1.place(x=100, y=150, width=300, height=30)
        label2.place(x=100, y=200, width=150, height=30)
        entry2.place(x=270, y=200, width=130, height=30)
        button1.place(x=100, y=250, width=300, height=30)
        button2.place(x=100, y=290, width=300, height=30)


        canvas2.pack(expand=YES, fill=BOTH)
        main_window.mainloop()


    def uni():
        # Frame4
        frame4 = Frame(main_window)
        frame2.destroy()

        def plot_uni():
            # Uniform linear Antenna Array
            freq = 10e6 # Set the operating frequency of the dipole in Hz
            wavelength = 3e8/freq # Calculate the wavelength of the signal

            lmda = 1
            #################################
            d = float(Fraction(entry2.get()))          # Antenna Length
            N = float(Fraction(entry3.get()))           # Number of elements
            alpha = float(Fraction(entry4.get()))    # Phase shift
            #################################
            beta = 2*np.pi/lmda; # bita
            phi = np.linspace(0, 2*np.pi, 360)

            # Set the number of points to calculate the radiation pattern
            theta = np.linspace(0, 2*np.pi, 360)
            gamma=np.linspace(0,2*np.pi,360)
            epsi=alpha+beta*d*np.cos(gamma);

            # Calculate the radiation pattern using the equation for a dipole antenna
            af=np.sin((N*epsi/2))/(N*np.sin((epsi/2)))
            af=np.abs(af)

            # Plot the polar radiation pattern
            plt.figure(1)
            plt.plot(epsi, af)
            plt.xlabel('Angle (radians)')
            plt.ylabel('Radiation pattern (dB)')
            plt.title('radiation pattern of a Uniform linear Array antenna')

            fig = plt.figure(2)
            ax = fig.add_subplot(111, projection='polar')
            ax.plot(phi, af)
            ax.set_title('Polar radiation pattern of a Uniform linear Array antenna')

            plt.show()

        def back_home():
            frame4.destroy()
            antennaGenerate()

        Antenna_image2 = PhotoImage(file="bilder/emty.png")
        canvas2 = Canvas(frame4, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
        canvas2.create_image(0, 0, image=Antenna_image2, anchor=NW)

        label1 = Label(frame4, text=" Write Antenna Parameters : ", bg="#5e4e3f", fg="white", relief="flat")

        label2 = Label(frame4, text=" Spacing(d) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry2 = Entry(frame4)
        label3 = Label(frame4, text=" Number of Elements(N) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry3 = Entry(frame4)
        label4 = Label(frame4, text=" Phase Shift(alpha) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry4 = Entry(frame4)

        button1 = Button(frame4, text=" Plot ", command=plot_uni, bg="white", fg="#5e4e3f", relief="raised", activebackground="#f3951e")
        button2 = Button(frame4, text=" Back ", command=back_home, bg="white", fg="#5e4e3f", relief="raised", activebackground="#f3951e")

        frame4.place(x=0, y=0,width=1215, height=700)
        label1.place(x=100, y=150, width=300, height=30)
        label2.place(x=100, y=200, width=150, height=30)
        label3.place(x=100, y=240, width=150, height=30)
        label4.place(x=100, y=280, width=150, height=30)
        entry2.place(x=270, y=200, width=130, height=30)
        entry3.place(x=270, y=240, width=130, height=30)
        entry4.place(x=270, y=280, width=130, height=30)
        button1.place(x=100, y=320, width=300, height=30)
        button2.place(x=100, y=360, width=300, height=30)

        canvas2.pack(expand=YES, fill=BOTH)
        main_window.mainloop()


    def binomial():
        # Frame5
        frame5 = Frame(main_window)
        frame2.destroy()

        def plot_bio():
            # Binomial Antenna
            freq = 10e6 # Set the operating frequency of the dipole in Hz
            wavelength = 3e8/freq # Calculate the wavelength of the signal

            lmda = 1
            #################################
            d =float(Fraction(entry2.get()))           # Antenna Length
            N = float(Fraction(entry3.get()))           # Number of elements
            alpha = float(Fraction(entry4.get()))    # Phase shift
            #################################
            beta = 2*np.pi/lmda; # bita
            phi = np.linspace(0, 2*np.pi, 360)

            # Set the number of points to calculate the radiation pattern
            theta = np.linspace(0, np.pi, 360)
            gamma=np.linspace(0,2*np.pi,360)
            epsi=alpha+beta*d*np.cos(gamma);

            # Calculate the radiation pattern using the equation for a dipole antenna
            U=epsi/2;
            af=np.power(np.cos(U),(N-1))
            af=np.abs(af)

            # Plot the polar radiation pattern
            plt.figure(1)
            plt.plot(epsi, af)
            plt.xlabel('Angle (radians)')
            plt.ylabel('Radiation pattern (dB)')
            plt.title('radiation pattern of a Binomial Array antenna')

            fig = plt.figure(2)
            ax = fig.add_subplot(111, projection='polar')
            ax.plot(phi, af)
            ax.set_title('Polar radiation pattern of a Binomial Array antenna')

            plt.show()


        def back_home():
            frame5.destroy()
            antennaGenerate()

        Antenna_image2 = PhotoImage(file="bilder/emty.png")
        canvas2 = Canvas(frame5, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
        canvas2.create_image(0, 0, image=Antenna_image2, anchor=NW)

        label1 = Label(frame5, text=" Write Antenna Parameters : ", bg="#5e4e3f", fg="white", relief="flat")

        label2 = Label(frame5, text=" Spacing(d) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry2 = Entry(frame5)
        label3 = Label(frame5, text=" Number of Elements(N) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry3 = Entry(frame5)
        label4 = Label(frame5, text=" Phase Shift(alpha) : ", bg="#5e4e3f", fg="white", relief="flat")
        entry4 = Entry(frame5)

        button1 = Button(frame5, text=" Plot ", command=plot_bio, bg="white", fg="#5e4e3f", relief="raised", activebackground="#f3951e")
        button2 = Button(frame5, text=" Back ", command=back_home, bg="white", fg="#5e4e3f", relief="raised", activebackground="#f3951e")

        frame5.place(x=0, y=0,width=1215, height=700)
        label1.place(x=100, y=150, width=300, height=30)
        label2.place(x=100, y=200, width=150, height=30)
        label3.place(x=100, y=240, width=150, height=30)
        label4.place(x=100, y=280, width=150, height=30)
        entry2.place(x=270, y=200, width=130, height=30)
        entry3.place(x=270, y=240, width=130, height=30)
        entry4.place(x=270, y=280, width=130, height=30)
        button1.place(x=100, y=320, width=300, height=30)
        button2.place(x=100, y=360, width=300, height=30)


        canvas2.pack(expand=YES, fill=BOTH)
        main_window.mainloop()

    Antenna_image2 = PhotoImage(file="bilder/emty.png")
    canvas2 = Canvas(frame2, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
    canvas2.create_image(0, 0, image=Antenna_image2, anchor=NW)

    label1 = Label(frame2, text=" Select Antenna Type : ", bg="#5e4e3f", fg="white", relief="flat")

    # Antenna types here
    button1 = Button(frame2, text="Dipole Antenna", command=dipole)
    button2 = Button(frame2, text="Uniform Linear Array Antenna", command=uni)
    button3 = Button(frame2, text="Binomial array Antenna", command=binomial)


    frame2.place(x=0, y=0,width=1215, height=700)
    label1.place(x=100, y=150, width=300, height=30)
    button1.place(x=100, y=200, width=300, height=30)
    button2.place(x=100, y=240, width=300, height=30)
    button3.place(x=100, y=280, width=300, height=30)

    canvas2.pack(expand=YES, fill=BOTH)

    main_window.mainloop()


def progress():
    button1.place_forget()

    # Change progress bar color
    style1 = ttk.Style()
    style1.theme_use('clam')
    style1.configure("red.Horizontal.TProgressbar", background="#5e4e3f", troughcolor="white")
    progress_bar = ttk.Progressbar(frame1, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=300, mode="determinate")
    progress_bar.place(x=200, y=460)
    progress_bar["value"] = 0
    while True:
        main_window.update()
        progress_bar["value"] += 5
        time.sleep(.05)
        if progress_bar["value"] >= 100:
            break
    frame1.destroy()
    antennaGenerate()

# Frame1
frame1 = Frame(main_window)

Antenna_image = PhotoImage(file="bilder/antenna1.png")

# Create canvases
canvas1 = Canvas(frame1, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
canvas1.create_image(0, 0, image=Antenna_image, anchor=NW)

# Create a button
button1 = Button(frame1, text="START", font=("Titan One", 25), bg="#5e4e3f", fg="white", borderwidth="4", relief="flat", command=progress)


#status_bar2 = Label(main_window, text=f"@ Abdelrahman Magdy ", font=(20), bd=0, anchor=W, bg="white", fg="black")
#status_bar2.place(x=2, y=680)

# Pack
frame1.place(x=0, y=0,width=1215, height=700)
button1.place(x=245, y=436, width=191, height=64)
canvas1.pack(expand=YES, fill=BOTH)

main_window.mainloop()
