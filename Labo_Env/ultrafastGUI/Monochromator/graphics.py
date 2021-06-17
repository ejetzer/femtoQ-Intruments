"""monochromator.graphics - Affichage & contrôle du monochromateur.

Par Émile Jetzer
Basé sur un programme par Nicolas Perron
"""


class Dialog:
    def __init__(self, parent_frame=None, main_phs=None):
        self.text = (
            "This method allows you to connect a single devices via the embeded graphical interface "
            "from GCS DLL. The first field is requiered. The second allows you to recall data and"
            " settings from this key."
        )
        self.frame = tk.Frame(parent_frame)
        dev_lbl = tk.Label(self.frame, text="Device name:")
        dev_lbl.grid(row=0, column=0, sticky="nw")
        login_lbl = tk.Label(self.frame, text="Login key:")
        login_lbl.grid(row=2, column=0, sticky="nw")
        dev_var = tk.StringVar()
        dev_entry = tk.Entry(self.frame, width=8, textvariable=dev_var)
        login_var = tk.StringVar()
        login_entry = tk.Entry(
            self.frame, width=8, textvariable=login_var)
        dev_entry.grid(row=1, column=0, sticky="nsew")
        login_entry.grid(row=3, column=0, sticky="nsew")
        con_b = tk.Button(
            self.frame,
            text="Connect Device(s)",
            command=lambda: messagebox.showinfo(
                title="Sorry", message="Script not written"
            ),
        )
        con_b.grid(row=4, column=0, sticky="nsew")


class Rs232:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame)
        com_lbl = tk.Label(self.frame, text="COM port")
        com_var = tk.StringVar()
        com_e = tk.Entry(
            self.frame, textvariable=com_var, width=10)
        com_lbl.grid(row=0, column=0, sticky="nw")
        com_e.grid(row=1, column=0, sticky="nsew")
        baud_lbl = tk.Label(self.frame, text="Baudrate")
        baud_var = tk.IntVar()
        baud_e = tk.Entry(
            self.frame, textvariable=baud_var, width=10)
        baud_lbl.grid(row=2, column=0, sticky="nw")
        baud_e.grid(row=3, column=0, sticky="nsew")
        con_b = tk.Button(
            self.frame,
            text="Connect Device(s)",
            command=lambda: messagebox.showinfo(
                title="Sorry", message="Script not written"
            ),
        )
        con_b.grid(row=4, column=0, sticky="nsew")


class Usb:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame)
        serial_lbl = tk.Label(
            self.frame, text="Serial number:")
        serial_var = tk.StringVar()
        serial_e = tk.Entry(
            self.frame, textvariable=serial_var, width=10
        )
        serial_lbl.grid(row=0, column=0, sticky="nw")
        serial_e.grid(row=1, column=0, sticky="nsew")
        con_b = tk.Button(
            self.frame,
            text="Connect Device(s)",
            command=lambda: messagebox.showinfo(
                title="Sorry", message="Script not written"
            ),
        )
        con_b.grid(row=4, column=0, sticky="nsew")


class Descript:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame)
        descrip_lbl = tk.Label(self.frame, text="Description")
        descrip_var = tk.StringVar()
        descrip_e = tk.Entry(
            self.frame, textvariable=descrip_var, width=10
        )
        descrip_lbl.grid(row=0, column=0, sticky="nw")
        descrip_e.grid(row=1, column=0, sticky="nsew")
        con_b = tk.Button(
            self.frame,
            text="Connect Device(s)",
            command=lambda: messagebox.showinfo(
                title="Sorry", message="Script not written"
            ),
        )
        con_b.grid(row=4, column=0, sticky="nsew")


class Adress:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame)
        ip_adress_lbl = tk.Label(self.frame, text="IP Adress:")
        ip_adress_var = tk.StringVar()
        ip_adress_e = tk.Entry(
            self.frame, textvariable=ip_adress_var, width=10
        )
        ip_adress_lbl.grid(row=0, column=0, sticky="nw")
        ip_adress_e.grid(row=1, column=0, sticky="nsew")
        port_lbl = tk.Label(self.frame, text="IP Port:")
        port_var = tk.IntVar()
        port_e = tk.Entry(
            self.frame, textvariable=port_var, width=10)
        port_lbl.grid(row=2, column=0, sticky="nw")
        port_e.grid(row=3, column=0, sticky="nsew")
        con_b = tk.Button(
            self.frame,
            text="Connect Device(s)",
            command=lambda: messagebox.showinfo(
                title="Sorry", message="Script not written"
            ),
        )
        con_b.grid(row=4, column=0, sticky="nsew")


class Interface:
    def __init__(self, parent_frame=None, main_phs=None):

        self.text = (
            "This method allows you to connect a single devices via characteristics of the device. "
            "Here is a quick decription of every characteristics: \nCOM port : Number of the COM port"
            " devices is connected to. \nBaudrate : Connexion speed of the device/transfer rate of "
            "the data. \nIP adress: IP adress associated with the device. IP port : IP port the "
            "device is connected to. \nDescription: Description of the device you want to connect."
        )
        self.frame = tk.Frame(parent_frame)
        choice = tk.StringVar()
        rs_232 = tk.Radiobutton(
            self.frame,
            text="RS-232",
            variable=choice,
            value="RS-232",
            command=lambda: self.frame_switch(choice),
        )
        usb = tk.Radiobutton(
            self.frame,
            text="USB",
            variable=choice,
            value="USB",
            command=lambda: self.frame_switch(choice),
        )
        desc = tk.Radiobutton(
            self.frame,
            text="TCP/IP: Description",
            variable=choice,
            value="Description",
            command=lambda: self.frame_switch(choice),
        )
        adress = tk.Radiobutton(
            self.frame,
            text="TCP/IP: Adress",
            variable=choice,
            value="Adress",
            command=lambda: self.frame_switch(choice),
        )
        choice.set("RS-232")
        self.dict_ = {
            "RS-232": Rs232(parent_frame=self.frame),
            "USB": Usb(parent_frame=self.frame),
            "Description": Descript(parent_frame=self.frame),
            "Adress": Adress(parent_frame=self.frame),
        }
        rs_232.grid(row=0, column=0, sticky="nw")
        usb.grid(row=1, column=0, sticky="nw")
        desc.grid(row=2, column=0, sticky="nw")
        adress.grid(row=3, column=0, sticky="nw")

    def frame_switch(self, new):
        new = new.get()
        for option in self.dict_:
            self.dict_[option].frame.grid_forget()
        self.dict_[new].frame.grid(
            column=0, row=4, sticky="nsew", rowspan=4, padx=5
        )


class DaisyChain:
    def __init__(self, parent_frame=None, main_phs=None):

        self.text = (
            "This method allows you to connect multiple devices via an interface. When connected each"
            " devices will receive a different ID to be controlled in the program."
        )
        self.frame = tk.Frame(parent_frame)
        choice = tk.StringVar()
        rs_232 = tk.Radiobutton(
            self.frame,
            text="RS-232",
            variable=choice,
            value="RS-232",
            command=lambda: self.frame_switch(choice),
        )
        usb = tk.Radiobutton(
            self.frame,
            text="USB",
            variable=choice,
            value="USB",
            command=lambda: self.frame_switch(choice),
        )
        desc = tk.Radiobutton(
            self.frame,
            text="TCP/IP: Description",
            variable=choice,
            value="Description",
            command=lambda: self.frame_switch(choice),
        )
        adress = tk.Radiobutton(
            self.frame,
            text="TCP/IP: Adress",
            variable=choice,
            value="Adress",
            command=lambda: self.frame_switch(choice),
        )
        choice.set("RS-232")
        self.dict_ = {
            "RS-232": Rs232(parent_frame=self.frame),
            "USB": Usb(parent_frame=self.frame),
            "Description": Descript(parent_frame=self.frame),
            "Adress": Adress(parent_frame=self.frame),
        }
        rs_232.grid(row=0, column=0, sticky="nw")
        usb.grid(row=1, column=0, sticky="nw")
        desc.grid(row=2, column=0, sticky="nw")
        adress.grid(row=3, column=0, sticky="nw")

    def frame_switch(self, new):
        new = new.get()
        for option in self.dict_:
            self.dict_[option].frame.grid_forget()
        self.dict_[new].frame.grid(
            column=0, row=4, sticky="nsew", rowspan=4, padx=5
        )


class Identification:
    def __init__(self, parent_frame=None, main_phs=None):
        self.text = (
            "This method allows you to connect a single device via a USB/IP scanning method. Inputs"
            " needs to either be a part of the name of the device you are looking for or a part of"
            " its IP adress."
        )
        self.frame = tk.Frame(parent_frame)
        usb_lbl = tk.Label(self.frame, text="Device name:")
        usb_lbl.grid(row=0, column=0, sticky="nw")
        ip_lbl = tk.Label(self.frame, text="IP adress:")
        ip_lbl.grid(row=2, column=0, sticky="nw")
        usb_var = tk.StringVar()
        usb_var.set("C-891")
        usb_entry = tk.Entry(self.frame, width=8, textvariable=usb_var)
        ip_var = tk.StringVar()
        ip_entry = tk.Entry(self.frame, width=8, textvariable=ip_var)
        usb_entry.grid(row=1, column=0, sticky="nsew")
        ip_entry.grid(row=3, column=0, sticky="nsew")
        if main_phs.mainf == None:
            con_b = tk.Button(
                self.frame,
                text="Connect Device(s)",
                command=lambda: main_phs.Linstage.connect_identification(
                    dev_name=usb_var, dev_ip=ip_var, exp_dependencie=False
                ),
            )
        else:
            con_b = tk.Button(
                self.frame,
                text="Connect Device(s)",
                command=lambda: main_phs.Linstage.connect_identification(
                    dev_name=usb_var, dev_ip=ip_var, exp_dependencie=True
                ),
            )

        con_b.grid(row=4, column=0, sticky="nsew")


class Mono_Physics(tk.Frame):

    def __update_speed(self, scale, variable):
        scale.configure(label="{}".format(variable[scale.get()]))
        self.Linstage.change_speed(factor=scale.get())

    def __init__(self, parent, mainf=None):

        super().__init__(parent)
        self.parent = parent
        self.mainf = mainf
        self.Mono = Monochromator.MonoChrom(mainf=mainf)  # TODO
        self.Linstage = Physics_Instrument.LinearStage(mainf=mainf)
        self.config(bg="gray", width=100, height=100)
        # Monochromator Stuff
        mono_frame = ttk.LabelFrame(self, text="Monochromator")
        mono_frame.grid(row=0, column=0, sticky="nsew")
        # This frame has lot of free space right now kinda disturbing
        mono_connect_b = tk.Button(
            mono_frame,
            text="Connect",
            width=8,
            command=lambda: self.Mono.connect(exp_dependencie=True),
        )
        mono_connect_b.grid(row=0, column=0, sticky="nsew")
        wave_lbl = tk.Label(mono_frame, text="Wavelength")
        wave_lbl.grid(row=2, column=0, sticky="nw")
        wave_entry_var = tk.IntVar()
        wave_entry = tk.Entry(mono_frame, textvariable=wave_entry_var, width=6)
        wave_entry.bind(
            "<Return>", lambda e: self.Mono.roll_dial(wave_entry_var.get()))
        wave_entry.grid(row=3, column=0, sticky="nsew")
        if self.mainf == None:
            calibrate_b = tk.Button(
                mono_frame,
                text="Calibrate",
                width=8,
                command=lambda: print(
                    "Option not available in independant window"),
            )
        else:
            calibrate_b = tk.Button(
                mono_frame,
                text="Calibrate",
                width=8,
                command=lambda: self.Mono.calibrate(
                    self.mainf.Frame[3].Spectro.spectro, wave_entry_var
                ),
            )
        calibrate_b.grid(row=1, column=0, sticky="nsew")
        # Physics Linear Stage Stuff
        phs_frame = ttk.LabelFrame(self, text="Physics Linear Stage")
        phs_frame.grid(row=0, column=1, columnspan=3, sticky="nsew")

        phs_con_frame = tk.Frame(phs_frame)
        phs_con_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        con_meth = ttk.Combobox(
            phs_con_frame, width=16, state="readonly", textvariable=""
        )
        con_meth["value"] = ("Dialog", "Interface",
                             "Identification", "Daisy Chain")
        con_meth.current(2)
        con_meth.grid(row=0, column=0, sticky="nw")
        con_meth.bind(
            "<<ComboboxSelected>>", lambda e: self.frame_switch(
                con_meth, textb)
        )

        phs_control = tk.Frame(phs_frame)
        phs_control.grid(row=2, column=0, rowspan=3, sticky="nsew")

        textb = tk.Text(
            phs_con_frame, width=50, height=16, wrap="word", state="disabled"
        )
        textb.grid(row=1, column=0, sticky="nsew")

        self.list_ = [
            Dialog(parent_frame=phs_con_frame, main_phs=self),
            Interface(parent_frame=phs_con_frame, main_phs=self),
            Identification(parent_frame=phs_con_frame, main_phs=self),
            DaisyChain(parent_frame=phs_con_frame, main_phs=self),
        ]
        self.frame_switch(con_meth, textb)
        for i in range(5):
            phs_frame.grid_rowconfigure(i, weight=1)
        phs_frame.grid_columnconfigure(0, weight=1)

        s = ttk.Separator(phs_control, orient="horizontal")
        s.grid(row=0, column=0, columnspan=20, sticky="nsew")
        scanning = tk.Label(phs_control, text="Scanning")
        scanning.grid(row=1, column=0, columnspan=2, sticky="nw")
        pos_lbl = tk.Label(phs_control, text="Position:")
        pos_lbl.grid(row=2, column=0, sticky="nw", pady=3)
        max_pos = tk.Label(phs_control, text="Max:")
        max_pos.grid(row=3, column=0, sticky="nw", pady=3)
        min_pos = tk.Label(phs_control, text="Min:")
        min_pos.grid(row=3, column=1, sticky="nw", pady=3)
        max_evar = tk.DoubleVar()
        max_evar.set(40)
        min_evar = tk.DoubleVar()
        min_evar.set(39.99)
        max_e = tk.Entry(phs_control, textvariable=max_evar, width=8)
        min_e = tk.Entry(phs_control, textvariable=min_evar, width=8)
        max_e.grid(row=4, column=0, sticky="nsew", padx=3)
        min_e.grid(row=4, column=1, sticky="nsew", padx=3)
        ite_var = tk.IntVar()
        ite_var.set(1)
        ite_e = tk.Entry(phs_control, width=6, textvariable=ite_var)
        ite_e.grid(row=5, column=1, sticky="nsew", padx=3)
        ite_lbl = tk.Label(phs_control, text="# Iteration :")
        ite_lbl.grid(row=5, column=0, sticky="nw", padx=3)

        # Entries for the scan and measure function
        step = tk.DoubleVar()
        step.set(0.02)  # um
        step_e = tk.Entry(phs_control, textvariable=step, width=8)
        step_e.grid(row=6, column=1, sticky="nsew", padx=3)
        step_text = tk.Label(phs_control, text="stage step (um)")
        step_text.grid(row=6, column=0, sticky="nsew", padx=3)
        duree = tk.DoubleVar()
        duree.set(300)
        duree_entry = tk.Entry(phs_control, width=6, textvariable=duree)
        duree_entry.grid(row=7, column=1, sticky="nsew", padx=3)
        duree_text = tk.Label(
            phs_control, text="measure duration per point (ms)")
        duree_text.grid(row=7, column=0, sticky="nsew", padx=3)

        # Here we should add a step size for the linear stage due the short time I have left I am skipping this part
        # I don't know what should be the best way to implement this quickly and the best way
        scan_b = tk.Button(
            phs_control,
            text="SCAN",
            width=8,
            command=lambda: threading.Thread(
                target=self.Linstage.scanning,
                args=(min_evar, max_evar, ite_var, duree, step),
            ).start(),
        )
        scan_b.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=3)

        # New column in the software for measures without scans (again temporary solution)
        s3 = ttk.Separator(phs_control, orient="vertical")
        s3.grid(row=0, column=14, rowspan=20, sticky="nsew")
        s4 = ttk.Separator(phs_control, orient="horizontal")
        s4.grid(row=0, column=10, columnspan=3)
        measure_only = tk.Label(phs_control, text="Measure only")
        measure_only.grid(row=1, column=11, sticky="nsew", columnspan=2)
        file_measure = tk.StringVar()
        file_measure.set("data")
        filem_entry = tk.Entry(phs_control, width=6, textvariable=file_measure)
        filem_entry.grid(row=2, column=12, sticky="nsew", padx=3)
        filem_text = tk.Label(phs_control, text="name of the saved file")
        filem_text.grid(row=2, column=11, sticky="nsew", padx=3)
        duree_m = tk.DoubleVar()
        duree_m.set(1.0)
        dureem_entry = tk.Entry(phs_control, width=6, textvariable=duree_m)
        dureem_entry.grid(row=3, column=12, sticky="nsew", padx=3)
        dureem_text = tk.Label(phs_control, text="measure duration (s)")
        dureem_text.grid(row=3, column=11, sticky="nsew", padx=3)

        s1 = ttk.Separator(phs_control, orient="vertical")
        s1.grid(row=0, column=2, rowspan=20, sticky="nsew")
        config = tk.Label(phs_control, text="Configure")
        config.grid(row=1, column=3, sticky="nw", columnspan=2)
        speed = tk.Label(phs_control, text="Velocity:")
        speed.grid(row=2, column=3, sticky="nw")
        speed_value = [
            "Slow",
            "Medium",
            "Quick",
            "U-Fast",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
        ]
        speed_scale = tk.Scale(
            phs_control,
            orient="horizontal",
            from_=0,
            to=9,
            width=16,
            showvalue=False,
            length=150,
            command=lambda x: update_speed(speed_scale, speed_value),
        )
        speed_scale.configure(label="{}".format(
            speed_value[speed_scale.get()]))
        speed_scale.grid(row=3, column=3, columnspan=2, sticky="nsew")
        calib_lin = tk.Button(
            phs_control,
            text="Calibrate device",
            width=16,
            command=lambda: self.Linstage.calibration(),
        )
        calib_lin.grid(row=6, column=3, columnspan=2, sticky="nsew", padx=3)
        s2 = ttk.Separator(phs_control, orient="vertical")
        s2.grid(row=0, column=5, sticky="nsew", padx=2, rowspan=20)
        control = tk.Label(phs_control, text="Control")
        control.grid(row=1, column=6, columnspan=2, sticky="nw")
        go2 = tk.Label(phs_control, text="Go to position:")
        go2.grid(row=2, column=6, sticky="nw")
        go_var = tk.DoubleVar()
        go_e = tk.Entry(phs_control, width=8, textvariable=go_var)
        go_e.grid(row=2, column=7, sticky="nsew", padx=2, pady=2)
        go_e.bind("<Return>", lambda e: self.Linstage.go_2position(go_var))
        inc = tk.Label(phs_control, text="Increment:")
        inc.grid(row=3, column=6, sticky="nw")
        inc_var = tk.DoubleVar()
        inc_e = tk.Entry(phs_control, width=8, textvariable=inc_var)
        inc_e.grid(row=3, column=7, sticky="nsew", padx=2, pady=2)
        left_b = tk.Button(
            phs_control,
            text="L",
            command=lambda: self.Linstage.increment_move(
                position=go_var, increment=inc_var, direction="left"
            ),
        )
        right_b = tk.Button(
            phs_control,
            text="R",
            command=lambda: self.Linstage.increment_move(
                position=go_var, increment=inc_var, direction="right"
            ),
        )
        left_b.grid(row=4, column=6, sticky="nsew", padx=2, pady=2)
        right_b.grid(row=4, column=7, sticky="nsew", padx=2, pady=2)
        s3 = ttk.Separator(phs_control, orient="vertical")
        s3.grid(row=0, column=8, sticky="nsew", rowspan=20)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def frame_switch(self, new, textbox):
        new = new.current()
        textbox.configure(state="normal")
        textbox.delete("1.0", tk.END)
        for class_ in self.list_:
            class_.frame.grid_forget()
        self.list_[new].frame.grid(
            column=1, row=0, sticky="nsew", rowspan=2, padx=5)
        textbox.insert("1.0", chars=self.list_[new].text)
        textbox.configure(state="disable")
