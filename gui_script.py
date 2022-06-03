import tkinter as tk
import webbrowser
import manage_settings as ms # to import settings

############################################# CLASS #################################
def start():
    class Application(tk.Tk):
        def __init__(self, *args, **kwargs):
            DATA = ms.config() # this ligne import the settings
            self.DATA = DATA
            tk.Tk.__init__(self, *args, **kwargs)
            self.wm_title(DATA["name"])
            self.title(DATA["name"])
            self.resizable(width=False,height=False)
            window_width, window_height = (600, 600)
            window_posx = int((self.winfo_screenwidth() - window_width) / 80)
            window_posy = int((self.winfo_screenheight() - window_height) / 2)
            geometry_arg = str(window_width) + "x" + str(window_height) + "+" + str(window_posx) + "+" + str(window_posy)
            self.geometry(geometry_arg)

            color_theme = [
                {
                    "color": "white",
                    "color2": "lightgrey",
                    "color3": "lightgrey"
                },
                {
                    "color": "white",
                    "color2": "cyan",
                    "color3": "pink",
                },
                {
                    "color":"black",
                    "color2":"grey",
                    "color3":"lightgrey"
                }
            ]
            self.color_theme = color_theme
            self.configure(bg=color_theme[0]["color"])

            # parameters frame
            parameters_box = tk.Frame(self)
            parameters_box.place(relx=0.3, rely=0.18, relwidth=0.675, relheight=0.75)
            self.parameters_box = parameters_box

            # list option frame
            option_frame = tk.Frame(self)
            option_frame.place(relx=0.025, rely=0.18, relwidth=0.25, relheight=0.75)
            self.option_frame = option_frame

            # banner frame
            banner = tk.Frame(self)
            banner.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.15)
            self.banner = banner

            # account in banner
            profile_img = tk.Frame(banner, width=90, height=50, bg='brown') # frame border : highlightbackground="red", highlightthickness=2
            profile_img.pack(side='left')
            self.profile_img = profile_img

            # pseudo in banner
            pseudo = tk.Label(banner, text="PSEUDO", width=40, height=4,  bg='green', borderwidth=2, relief="groove")
            pseudo.pack(side='left')
            self.pseudo = pseudo

            # home redirect button in banner
            home_img = tk.Frame(banner, width=90, height=60, bg='red')
            home_img.pack(side='left')
            self.home_img = home_img

            # help button in banner
            help_img = tk.Frame(banner, width=90, height=60, bg='white')
            help_img.pack(side='left')
            self.help_img = help_img

            account = Menu_buttons(option_frame, text="Account", command=account_settings).place_btn()
            keybind = Menu_buttons(option_frame, text="Keybind", command=keybinds_settings).place_btn()
            interface = Menu_buttons(option_frame, text="Interface", command=interface_settings).place_btn()
            preferences = Menu_buttons(option_frame, text="Preferences", command=preferences_settings).place_btn()
            voice = Menu_buttons(option_frame, text="Voice", command=test).place_btn()
            language = Menu_buttons(option_frame, text="Language", command=test).place_btn()
            appearance = Menu_buttons(option_frame, text="Appearance", command=test).place_btn()

    class Menu_buttons(tk.Button):
        y = 0.07 # position vertical

        def __init__(self, *args, **kwargs):
            tk.Button.__init__(self, *args, **kwargs)

        def place_btn(self):
            self.place(relx=0.04, rely=Menu_buttons.y, relwidth=0.90, relheight=0.1)
            Menu_buttons.y += 0.13

    ######################################### FUNCTIONS #################################
    def check_form(execute):
        validate_button = tk.Button(option.parameters_box, text="Valider", command=execute)
        validate_button.place(relx=0.87, rely=0.93)

    def account_settings():
        DATA = ms.config()
        for child in option.parameters_box.winfo_children():
                child.destroy()

        def change_in_site():
            url='https://google.com'
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)

        def change_pp():
            pass

        y = 0.04
        pseudo_name = DATA["user"]["name"] #get in settings
        pseudo_entry = tk.Entry(option.parameters_box)
        pseudo_entry.insert(0, pseudo_name)
        pseudo_entry.place(relx=0.04, rely=y, relwidth=0.60)
        pseudo_label = tk.Label(option.parameters_box, text=pseudo_name)
        pseudo_label.place(relx=0.65, rely=y, relwidth=0.3)

        mdp_change_btn = tk.Button(option.parameters_box, text="Change password", command=change_in_site) # go to website
        mdp_change_btn.place(relx=0.04, rely=y+0.1, relwidth=0.9, height=40)

        mail_change_btn = tk.Button(option.parameters_box, text="Change e-mail address", command=change_in_site) # go to website
        mail_change_btn.place(relx=0.04, rely=y+0.2, relwidth=0.9, height=40)

        change_pp_btn = tk.Button(option.parameters_box, text="Change profil picture", command=change_pp)
        change_pp_btn.place(relx=0.04, rely=y+0.3, relwidth=0.9, height=40)

        delete_account_btn = tk.Button(option.parameters_box, text="Delete Account", command=change_in_site) # go to website
        delete_account_btn.place(relx=0.04, rely=y+0.4, relwidth=0.9, height=40)

        def change_pseudo():
            name = pseudo_entry.get()
            # to do: name validation like  p*te == False
            # name len validation
            if len(name)<3:
                pseudo_label.configure(text="Pseudo is too short")
            elif len(name)>10:
                pseudo_label.configure(text="Pseudo is too long")
            else:
                pseudo_label.configure(text="Change valided")
                option.pseudo.configure(text=name)
                print(name)
                ms.modif(("user", "name"), name)

        def check_account_settings():
            change_pseudo()
            change_pp()

        check_form(check_account_settings)

    def interface_settings():
        for child in option.parameters_box.winfo_children():
                child.destroy()
                
        theme_menu_btn = tk.Menubutton(option.parameters_box, direction="below", text="Change Theme", relief="raised")
        theme_menu_btn.menu = tk.Menu(theme_menu_btn, tearoff=0)
        theme_menu_btn['menu'] = theme_menu_btn.menu
        def light():
            option.parameters_box.configure(bg=option.color_theme[1]['color2'])
            option.option_frame.configure(bg=option.color_theme[1]['color3'])
            option.configure(bg=option.color_theme[1]['color'])
        def dark():
            option.parameters_box.configure(bg=option.color_theme[2]['color2'])
            option.option_frame.configure(bg=option.color_theme[2]['color3'])
            option.configure(bg=option.color_theme[2]['color'])
        def default():
            option.parameters_box.configure(bg=option.color_theme[0]['color2'])
            option.option_frame.configure(bg=option.color_theme[0]['color3'])
            option.configure(bg=option.color_theme[0]['color'])
        theme_menu_btn.menu.add_command(label='Light', command=light)
        theme_menu_btn.menu.add_command(label='Dark', command=dark)
        theme_menu_btn.menu.add_command(label='Default', command=default)

        theme_menu_btn.place(relx=0.04, rely=0.04, relwidth=0.9, height=40)

    def preferences_settings():
        for child in option.parameters_box.winfo_children():
                child.destroy()

        launch = tk.BooleanVar()
        display = tk.BooleanVar()
        in_back = tk.BooleanVar()
        close_when = tk.BooleanVar()

        y = 0.04

        # label
        start_launch = tk.Label(option.parameters_box, text="launch at start", relief="raised")
        start_launch.place(relx=0.04, rely=y, relwidth=0.8, height=40)

        display_launch = tk.Label(option.parameters_box, text="display interface at start", relief="raised")
        display_launch.place(relx=0.04, rely=y+0.1, relwidth=0.8, height=40)

        launch_bg = tk.Label(option.parameters_box, text="launch in background", relief="raised")
        launch_bg.place(relx=0.04, rely=y+0.2, relwidth=0.8, height=40)

        close_moment = tk.Label(option.parameters_box, text="close at moment", relief="raised")
        close_moment.place(relx=0.04, rely=y+0.3, relwidth=0.8, height=40)

        # checkbox
        launch_start_case = tk.Checkbutton(option.parameters_box, onvalue=True, offvalue=False, variable=launch)
        launch_start_case.place(relx=0.88, rely=y, relwidth=0.08, height=40)

        display_launch_case = tk.Checkbutton(option.parameters_box, onvalue=True, offvalue=False, variable=display)
        display_launch_case.place(relx=0.88, rely=y+0.1, relwidth=0.08, height=40)

        launch_bg_case = tk.Checkbutton(option.parameters_box, onvalue=True, offvalue=False, variable=in_back)
        launch_bg_case.place(relx=0.88, rely=y+0.2, relwidth=0.08, height=40)

        close_moment_case = tk.Checkbutton(option.parameters_box, onvalue=True, offvalue=False, variable=close_when)
        close_moment_case.place(relx=0.88, rely=y+0.3, relwidth=0.08, height=40)

        def get_preferences():
            check_list = [launch.get(), display.get(), in_back.get(), close_when.get()]
            # create the code with settings.json below ...

        check_form(get_preferences)

    def keybinds_settings(): # to finish
        for child in option.parameters_box.winfo_children():
            child.destroy()

        y = 0.04
        y_change_bind = 0.06

        def show_display_key():
            # button.configure(text='stop changing keybinds')
            # code to change label ->
            pass

        show_display = tk.Label(option.parameters_box, text="Show display", relief="raised")
        show_display.place(relx=0.04, rely=y, relwidth=0.8, height=40)
        show_display_button = tk.Button(option.parameters_box, text="Change bind", command=show_display_key)
        show_display_button.place(relx=0.6, rely=y_change_bind, relwidth=0.2, height=20)

        vocal = tk.Label(option.parameters_box, text="Vocal on/off", relief="raised")
        vocal.place(relx=0.04, rely=y+0.1, relwidth=0.8, height=40)
        vocal_button = tk.Button(option.parameters_box, text="Change bind", command=show_display_key)
        vocal_button.place(relx=0.6, rely=y_change_bind+0.1, relwidth=0.2, height=20)

        search_google = tk.Label(option.parameters_box, text="Search on google", relief="raised")
        search_google.place(relx=0.04, rely=y+0.2, relwidth=0.8, height=40)
        search_google_button = tk.Button(option.parameters_box, text="Change bind", command=show_display_key)
        search_google_button.place(relx=0.6, rely=y_change_bind+0.2, relwidth=0.2, height=20)

        open_app = tk.Label(option.parameters_box, text="Open an app", relief="raised")
        open_app.place(relx=0.04, rely=y+0.3, relwidth=0.8, height=40)
        open_app_button = tk.Button(option.parameters_box, text="Change bind", command=show_display_key)
        open_app_button.place(relx=0.6, rely=y_change_bind+0.3, relwidth=0.2, height=20)

        writing_box = tk.Label(option.parameters_box, text="Write from writing box ", relief="raised") # writing box = box under interface Theo
        writing_box.place(relx=0.04, rely=y+0.4, relwidth=0.8, height=40)
        writing_box_button = tk.Button(option.parameters_box, text="Change bind", command=show_display_key)
        writing_box_button.place(relx=0.6, rely=y_change_bind+0.4, relwidth=0.2, height=20)

        display_key_text=("F1", "F2", "F3", "F4", "F5")

        show_display_keybinds = tk.Label(option.parameters_box, text=display_key_text[0], relief="raised")
        show_display_keybinds.place(relx=0.88, rely=y, relwidth=0.08, height=40)

        vocal_keybinds = tk.Label(option.parameters_box, text=display_key_text[1], relief="raised")
        vocal_keybinds.place(relx=0.88, rely=y+0.1, relwidth=0.08, height=40)

        search_google_keybinds = tk.Label(option.parameters_box, text=display_key_text[2], relief="raised")
        search_google_keybinds.place(relx=0.88, rely=y+0.2, relwidth=0.08, height=40)

        open_app_keybinds = tk.Label(option.parameters_box, text=display_key_text[3], relief="raised")
        open_app_keybinds.place(relx=0.88, rely=y+0.3, relwidth=0.08, height=40)

        write_box_keybinds = tk.Label(option.parameters_box, text=display_key_text[4], relief="raised")
        write_box_keybinds.place(relx=0.88, rely=y+0.4, relwidth=0.08, height=40)

        def get_keybinds():
            # keybinds_list = [show_display_keybinds.get(), vocal_keybinds.get(), search_google.get()]
            # create the code with settings.json below ...
            pass

        check_form(get_keybinds)

    def test():
        for child in option.parameters_box.winfo_children():
                child.destroy()
        pass

    ######################################### MAIN ALGO ################################

    option = Application()
    Menu_buttons.y = 0.07
    option.mainloop()

if __name__=='__main__':
        start()
